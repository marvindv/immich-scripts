# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.94.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from openapi_client.models.asset_type_enum import AssetTypeEnum
from openapi_client.models.exif_response_dto import ExifResponseDto
from openapi_client.models.person_with_faces_response_dto import PersonWithFacesResponseDto
from openapi_client.models.smart_info_response_dto import SmartInfoResponseDto
from openapi_client.models.tag_response_dto import TagResponseDto
from openapi_client.models.user_response_dto import UserResponseDto

class AssetResponseDto(BaseModel):
    """
    AssetResponseDto
    """
    checksum: StrictStr = Field(..., description="base64 encoded sha1 hash")
    device_asset_id: StrictStr = Field(..., alias="deviceAssetId")
    device_id: StrictStr = Field(..., alias="deviceId")
    duration: StrictStr = Field(...)
    exif_info: Optional[ExifResponseDto] = Field(None, alias="exifInfo")
    file_created_at: datetime = Field(..., alias="fileCreatedAt")
    file_modified_at: datetime = Field(..., alias="fileModifiedAt")
    has_metadata: StrictBool = Field(..., alias="hasMetadata")
    id: StrictStr = Field(...)
    is_archived: StrictBool = Field(..., alias="isArchived")
    is_external: StrictBool = Field(..., alias="isExternal")
    is_favorite: StrictBool = Field(..., alias="isFavorite")
    is_offline: StrictBool = Field(..., alias="isOffline")
    is_read_only: StrictBool = Field(..., alias="isReadOnly")
    is_trashed: StrictBool = Field(..., alias="isTrashed")
    library_id: StrictStr = Field(..., alias="libraryId")
    live_photo_video_id: Optional[StrictStr] = Field(None, alias="livePhotoVideoId")
    local_date_time: datetime = Field(..., alias="localDateTime")
    original_file_name: StrictStr = Field(..., alias="originalFileName")
    original_path: StrictStr = Field(..., alias="originalPath")
    owner: Optional[UserResponseDto] = None
    owner_id: StrictStr = Field(..., alias="ownerId")
    people: Optional[conlist(PersonWithFacesResponseDto)] = None
    resized: StrictBool = Field(...)
    smart_info: Optional[SmartInfoResponseDto] = Field(None, alias="smartInfo")
    stack: Optional[conlist(AssetResponseDto)] = None
    stack_count: Optional[StrictInt] = Field(..., alias="stackCount")
    stack_parent_id: Optional[StrictStr] = Field(None, alias="stackParentId")
    tags: Optional[conlist(TagResponseDto)] = None
    thumbhash: Optional[StrictStr] = Field(...)
    type: AssetTypeEnum = Field(...)
    updated_at: datetime = Field(..., alias="updatedAt")
    __properties = ["checksum", "deviceAssetId", "deviceId", "duration", "exifInfo", "fileCreatedAt", "fileModifiedAt", "hasMetadata", "id", "isArchived", "isExternal", "isFavorite", "isOffline", "isReadOnly", "isTrashed", "libraryId", "livePhotoVideoId", "localDateTime", "originalFileName", "originalPath", "owner", "ownerId", "people", "resized", "smartInfo", "stack", "stackCount", "stackParentId", "tags", "thumbhash", "type", "updatedAt"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> AssetResponseDto:
        """Create an instance of AssetResponseDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of exif_info
        if self.exif_info:
            _dict['exifInfo'] = self.exif_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in people (list)
        _items = []
        if self.people:
            for _item in self.people:
                if _item:
                    _items.append(_item.to_dict())
            _dict['people'] = _items
        # override the default output from pydantic by calling `to_dict()` of smart_info
        if self.smart_info:
            _dict['smartInfo'] = self.smart_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in stack (list)
        _items = []
        if self.stack:
            for _item in self.stack:
                if _item:
                    _items.append(_item.to_dict())
            _dict['stack'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in self.tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tags'] = _items
        # set to None if live_photo_video_id (nullable) is None
        # and __fields_set__ contains the field
        if self.live_photo_video_id is None and "live_photo_video_id" in self.__fields_set__:
            _dict['livePhotoVideoId'] = None

        # set to None if stack_count (nullable) is None
        # and __fields_set__ contains the field
        if self.stack_count is None and "stack_count" in self.__fields_set__:
            _dict['stackCount'] = None

        # set to None if stack_parent_id (nullable) is None
        # and __fields_set__ contains the field
        if self.stack_parent_id is None and "stack_parent_id" in self.__fields_set__:
            _dict['stackParentId'] = None

        # set to None if thumbhash (nullable) is None
        # and __fields_set__ contains the field
        if self.thumbhash is None and "thumbhash" in self.__fields_set__:
            _dict['thumbhash'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AssetResponseDto:
        """Create an instance of AssetResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AssetResponseDto.parse_obj(obj)

        _obj = AssetResponseDto.parse_obj({
            "checksum": obj.get("checksum"),
            "device_asset_id": obj.get("deviceAssetId"),
            "device_id": obj.get("deviceId"),
            "duration": obj.get("duration"),
            "exif_info": ExifResponseDto.from_dict(obj.get("exifInfo")) if obj.get("exifInfo") is not None else None,
            "file_created_at": obj.get("fileCreatedAt"),
            "file_modified_at": obj.get("fileModifiedAt"),
            "has_metadata": obj.get("hasMetadata"),
            "id": obj.get("id"),
            "is_archived": obj.get("isArchived"),
            "is_external": obj.get("isExternal"),
            "is_favorite": obj.get("isFavorite"),
            "is_offline": obj.get("isOffline"),
            "is_read_only": obj.get("isReadOnly"),
            "is_trashed": obj.get("isTrashed"),
            "library_id": obj.get("libraryId"),
            "live_photo_video_id": obj.get("livePhotoVideoId"),
            "local_date_time": obj.get("localDateTime"),
            "original_file_name": obj.get("originalFileName"),
            "original_path": obj.get("originalPath"),
            "owner": UserResponseDto.from_dict(obj.get("owner")) if obj.get("owner") is not None else None,
            "owner_id": obj.get("ownerId"),
            "people": [PersonWithFacesResponseDto.from_dict(_item) for _item in obj.get("people")] if obj.get("people") is not None else None,
            "resized": obj.get("resized"),
            "smart_info": SmartInfoResponseDto.from_dict(obj.get("smartInfo")) if obj.get("smartInfo") is not None else None,
            "stack": [AssetResponseDto.from_dict(_item) for _item in obj.get("stack")] if obj.get("stack") is not None else None,
            "stack_count": obj.get("stackCount"),
            "stack_parent_id": obj.get("stackParentId"),
            "tags": [TagResponseDto.from_dict(_item) for _item in obj.get("tags")] if obj.get("tags") is not None else None,
            "thumbhash": obj.get("thumbhash"),
            "type": obj.get("type"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj

AssetResponseDto.update_forward_refs()

