import sys
from pathlib import PurePath

import click
import openapi_client
from rich.progress import track

from .jobs import Job, SetAssetModifiedDate
from .log import log
from .utils import get_asset_host_path


@click.command(help="Fixes the modified date of assets uploaded with version <1.95.0")
@click.option("--api-key", help="Immich API key", required=True)
@click.option(
    "--api-host",
    help="Immich API endpoint, e.g. http://localhost:22283/api",
    required=True,
)
@click.option(
    "--host-upload-location",
    help="The UPLOAD_LOCATION directory (as defined in the .env file next to docker-compose.yml), "
    "i.e. the directory that contains among others the `library` and `upload` directories.",
    required=True,
)
@click.option("--dry-run", is_flag=True)
def main(
    api_key: str,
    api_host: str,
    host_upload_location: str,
    dry_run: bool,
) -> None:
    api_conf = openapi_client.Configuration(
        host=api_host,
    )
    api_conf.api_key["api_key"] = api_key

    with openapi_client.ApiClient(api_conf) as api_client:
        user_api = openapi_client.UserApi(api_client)
        asset_api = openapi_client.AssetApi(api_client)

        owner = user_api.get_my_user_info()

        asset_take = 2**32
        log.info(
            f"Loads up to {asset_take} assets, which is hopefully more than you have ..."
        )
        assets = asset_api.get_all_assets(take=asset_take)
        log.info(f"Loaded {len(assets)} assets.")

        jobs: list[Job] = []
        for asset in assets:
            # Ignore external assets.
            if asset.is_external:
                continue

            asset_path = PurePath(asset.original_path)
            try:
                host_path = get_asset_host_path(asset, owner, host_upload_location)
            except ValueError as ex:
                log.error(str(ex))
                sys.exit(1)

            if not host_path.exists():
                log.error(
                    f"Assumed host path of asset {asset_path} ({asset.id}) is {host_path} but the file does not exist. "
                    "Something is wrong. Aborting ..."
                )
                sys.exit(1)

            jobs.append(
                SetAssetModifiedDate(
                    asset, owner, host_upload_location, asset.file_modified_at
                )
            )

        log.info("All assets collected. Running collected jobs ...")
        for job in track(jobs, description="Processing..."):
            job.execute(dry_run)


if __name__ == "__main__":
    main()
