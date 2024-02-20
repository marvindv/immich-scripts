import sys
from pathlib import Path, PurePath

import click
import openapi_client
from rich.progress import track

from immich_scripts.jobs import BulkDeleteAssetJob, Job, MoveAssetJob, ScanLibraryJob
from immich_scripts.log import log


@click.command(
    help="Moves all assets in a specified album to another physical location "
    "(e.g. the directory of an external library)."
)
@click.option("--api-key", help="Immich API key", required=True)
@click.option(
    "--api-host",
    help="Immich API endpoint, e.g. http://localhost:22283/api",
    required=True,
)
@click.option(
    "--album-name",
    help="The name of the album that contains the images to move to the shared storage.",
    required=True,
)
@click.option(
    "--host-upload-location",
    help="The UPLOAD_LOCATION directory (as defined in the .env file next to docker-compose.yml), "
    "i.e. the directory that contains among others the `library` and `upload` directories.",
    required=True,
)
@click.option(
    "--target-location",
    help="The directory where to move the images to.",
    required=True,
)
@click.option(
    "--target-library-name",
    help="The name of the library that imports the target location. "
    "If set, starts a library scan for this library.",
)
@click.option("--dry-run", is_flag=True)
def cli(
    api_key: str,
    api_host: str,
    album_name: str,
    host_upload_location: str,
    target_location: str,
    target_library_name: str | None,
    dry_run: bool,
) -> None:
    api_conf = openapi_client.Configuration(
        host=api_host,
    )
    api_conf.api_key["api_key"] = api_key

    with openapi_client.ApiClient(api_conf) as api_client:
        album_api = openapi_client.AlbumApi(api_client)
        asset_api = openapi_client.AssetApi(api_client)
        library_api = openapi_client.LibraryApi(api_client)

        albums = album_api.get_all_albums()
        # Check whether the specified album exists.
        album = next((a for a in albums if a.album_name == album_name), None)
        if album is None:
            log.error(f"Album {album_name} not found")
            sys.exit(1)

        if album.asset_count == 0:
            log.info(f"Album {album_name} contains no assets. Nothing to do.")
            sys.exit(0)

        log.info("Album found. Collect assets ...")

        # Load assets of the album, add them to delete job and create move jobs.
        album_info = album_api.get_album_info(album.id)
        jobs: list[Job] = []
        delete_job = BulkDeleteAssetJob(asset_api)
        for asset in album_info.assets:
            if asset.is_external:
                log.warning(f"Skip external asset {asset.original_file_name}")
                continue

            asset_path = PurePath(asset.original_path)
            if (
                asset_path.parts[0] != "upload"
                or asset_path.parts[1] != "library"
                or asset_path.parts[2] != album.owner.storage_label
            ):
                log.error(
                    f"Asset {asset.original_file_name} ({asset.id}) unexpected path prefix: {asset_path}"
                )
                sys.exit(1)

            # Remove leading `upload/` from path and prepend the hosts upload location.
            host_path = Path(host_upload_location, *asset_path.parts[1:])
            target_path = Path(target_location, *asset_path.parts[3:])
            if not host_path.exists():
                log.error(
                    f"Assumed host path of asset {asset_path} ({asset.id}) is {host_path} but the file does not exist. "
                    "Something is wrong. Aborting ..."
                )
                sys.exit(1)

            jobs.append(MoveAssetJob(asset, host_path, target_path))
            delete_job.add_asset(asset, host_path)

        jobs.append(delete_job)
        log.info("All assets collected. Running collected jobs ...")

        if target_library_name is not None:
            libraries = library_api.get_libraries()
            library = next(
                (lib for lib in libraries if lib.name == target_library_name), None
            )
            if library is None:
                log.error(f"Library to scan {target_library_name} not found.")
                sys.exit(1)

            jobs.append(ScanLibraryJob(library, library_api))

        # Run collected jobs.
        for job in track(jobs, description="Processing..."):
            job.execute(dry_run)


if __name__ == "__main__":
    cli()
