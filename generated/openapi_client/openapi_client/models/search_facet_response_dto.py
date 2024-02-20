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


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist
from openapi_client.models.search_facet_count_response_dto import SearchFacetCountResponseDto

class SearchFacetResponseDto(BaseModel):
    """
    SearchFacetResponseDto
    """
    counts: conlist(SearchFacetCountResponseDto) = Field(...)
    field_name: StrictStr = Field(..., alias="fieldName")
    __properties = ["counts", "fieldName"]

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
    def from_json(cls, json_str: str) -> SearchFacetResponseDto:
        """Create an instance of SearchFacetResponseDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in counts (list)
        _items = []
        if self.counts:
            for _item in self.counts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['counts'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SearchFacetResponseDto:
        """Create an instance of SearchFacetResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SearchFacetResponseDto.parse_obj(obj)

        _obj = SearchFacetResponseDto.parse_obj({
            "counts": [SearchFacetCountResponseDto.from_dict(_item) for _item in obj.get("counts")] if obj.get("counts") is not None else None,
            "field_name": obj.get("fieldName")
        })
        return _obj


