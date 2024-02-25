from pathlib import Path, PurePath
from openapi_client.models.asset_response_dto import AssetResponseDto

from openapi_client.models.user_response_dto import UserResponseDto


def get_asset_host_path(
    asset: AssetResponseDto, owner: UserResponseDto, host_upload_location: str
) -> Path:
    asset_path = PurePath(asset.original_path)
    if (
        asset_path.parts[0] != "upload"
        or asset_path.parts[1] != "library"
        or asset_path.parts[2] != owner.storage_label
    ):
        raise ValueError(
            f"Asset {asset.original_file_name} ({asset.id}) unexpected path prefix: {asset_path}"
        )

    # Remove leading `upload/` from path and prepend the hosts upload location.
    host_path = Path(host_upload_location, *asset_path.parts[1:])
    return host_path
