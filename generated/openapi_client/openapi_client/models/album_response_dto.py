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
from openapi_client.models.asset_response_dto import AssetResponseDto
from openapi_client.models.user_response_dto import UserResponseDto

class AlbumResponseDto(BaseModel):
    """
    AlbumResponseDto
    """
    album_name: StrictStr = Field(..., alias="albumName")
    album_thumbnail_asset_id: Optional[StrictStr] = Field(..., alias="albumThumbnailAssetId")
    asset_count: StrictInt = Field(..., alias="assetCount")
    assets: conlist(AssetResponseDto) = Field(...)
    created_at: datetime = Field(..., alias="createdAt")
    description: StrictStr = Field(...)
    end_date: Optional[datetime] = Field(None, alias="endDate")
    has_shared_link: StrictBool = Field(..., alias="hasSharedLink")
    id: StrictStr = Field(...)
    is_activity_enabled: StrictBool = Field(..., alias="isActivityEnabled")
    last_modified_asset_timestamp: Optional[datetime] = Field(None, alias="lastModifiedAssetTimestamp")
    owner: UserResponseDto = Field(...)
    owner_id: StrictStr = Field(..., alias="ownerId")
    shared: StrictBool = Field(...)
    shared_users: conlist(UserResponseDto) = Field(..., alias="sharedUsers")
    start_date: Optional[datetime] = Field(None, alias="startDate")
    updated_at: datetime = Field(..., alias="updatedAt")
    __properties = ["albumName", "albumThumbnailAssetId", "assetCount", "assets", "createdAt", "description", "endDate", "hasSharedLink", "id", "isActivityEnabled", "lastModifiedAssetTimestamp", "owner", "ownerId", "shared", "sharedUsers", "startDate", "updatedAt"]

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
    def from_json(cls, json_str: str) -> AlbumResponseDto:
        """Create an instance of AlbumResponseDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in assets (list)
        _items = []
        if self.assets:
            for _item in self.assets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['assets'] = _items
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in shared_users (list)
        _items = []
        if self.shared_users:
            for _item in self.shared_users:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sharedUsers'] = _items
        # set to None if album_thumbnail_asset_id (nullable) is None
        # and __fields_set__ contains the field
        if self.album_thumbnail_asset_id is None and "album_thumbnail_asset_id" in self.__fields_set__:
            _dict['albumThumbnailAssetId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AlbumResponseDto:
        """Create an instance of AlbumResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AlbumResponseDto.parse_obj(obj)

        _obj = AlbumResponseDto.parse_obj({
            "album_name": obj.get("albumName"),
            "album_thumbnail_asset_id": obj.get("albumThumbnailAssetId"),
            "asset_count": obj.get("assetCount"),
            "assets": [AssetResponseDto.from_dict(_item) for _item in obj.get("assets")] if obj.get("assets") is not None else None,
            "created_at": obj.get("createdAt"),
            "description": obj.get("description"),
            "end_date": obj.get("endDate"),
            "has_shared_link": obj.get("hasSharedLink"),
            "id": obj.get("id"),
            "is_activity_enabled": obj.get("isActivityEnabled"),
            "last_modified_asset_timestamp": obj.get("lastModifiedAssetTimestamp"),
            "owner": UserResponseDto.from_dict(obj.get("owner")) if obj.get("owner") is not None else None,
            "owner_id": obj.get("ownerId"),
            "shared": obj.get("shared"),
            "shared_users": [UserResponseDto.from_dict(_item) for _item in obj.get("sharedUsers")] if obj.get("sharedUsers") is not None else None,
            "start_date": obj.get("startDate"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj

