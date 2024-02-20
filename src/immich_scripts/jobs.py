import os
import shutil
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path

import openapi_client
from openapi_client.models.asset_bulk_delete_dto import AssetBulkDeleteDto
from openapi_client.models.asset_response_dto import AssetResponseDto
from openapi_client.models.library_response_dto import LibraryResponseDto
from openapi_client.models.scan_library_dto import ScanLibraryDto

from .log import log


class Job(ABC):
    @abstractmethod
    def _dry_run(self) -> None:
        pass

    @abstractmethod
    def _run(self) -> None:
        pass

    def execute(self, dry_run: bool) -> None:
        if dry_run:
            self._dry_run()
        else:
            self._run()


class MoveAssetJob(Job):
    """Move one asset from host_path to target_path."""

    def __init__(self, asset: AssetResponseDto, host_path: Path, target_path: Path):
        super().__init__()
        self._asset = asset
        self._host_path = host_path
        self._target_path = target_path

    def _dry_run(self) -> None:
        log.info(f"Would move {self._host_path} -> {self._target_path}")

    def _run(self) -> None:
        # Ensure target directory exists.
        self._target_path.parent.mkdir(parents=True, exist_ok=True)
        # Copy image to shared location, then delete the asset.
        shutil.copy2(self._host_path, self._target_path)
        # This is probably no longer necessary as soon as
        # https://github.com/immich-app/immich/pull/7010 is merged and released.
        os.utime(
            self._target_path,
            (datetime.now().timestamp(), self._asset.file_modified_at.timestamp()),
        )


Job.register(MoveAssetJob)


class BulkDeleteAssetJob(Job):
    """Deletes many assets."""

    def __init__(self, asset_api: openapi_client.AssetApi) -> None:
        super().__init__()
        self._assets: list[tuple[AssetResponseDto, Path]] = []
        self._asset_api = asset_api

    def _dry_run(self) -> None:
        for asset, host_path in self._assets:
            log.info(f"Would delete asset {host_path} ({asset.id})")

    def _run(self) -> None:
        self._asset_api.delete_assets(
            AssetBulkDeleteDto(ids=[asset.id for asset, _ in self._assets])
        )

    def add_asset(self, asset: AssetResponseDto, host_path: Path) -> None:
        self._assets.append((asset, host_path))


Job.register(BulkDeleteAssetJob)


class ScanLibraryJob(Job):
    """Initiates a library scan."""

    def __init__(
        self, library: LibraryResponseDto, library_api: openapi_client.LibraryApi
    ) -> None:
        super().__init__()
        self._library = library
        self._library_api = library_api

    def _dry_run(self) -> None:
        log.info(f"Would scan library {self._library.name} ({self._library.id})")

    def _run(self) -> None:
        self._library_api.scan_library(
            self._library.id,
            ScanLibraryDto(
                refreshAllFiles=False,
                refreshModifiedFiles=False,
            ),
        )


Job.register(ScanLibraryJob)
