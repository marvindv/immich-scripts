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
from pydantic import BaseModel, Field, StrictInt, conlist
from openapi_client.models.person_response_dto import PersonResponseDto

class PeopleResponseDto(BaseModel):
    """
    PeopleResponseDto
    """
    people: conlist(PersonResponseDto) = Field(...)
    total: StrictInt = Field(...)
    __properties = ["people", "total"]

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
    def from_json(cls, json_str: str) -> PeopleResponseDto:
        """Create an instance of PeopleResponseDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in people (list)
        _items = []
        if self.people:
            for _item in self.people:
                if _item:
                    _items.append(_item.to_dict())
            _dict['people'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PeopleResponseDto:
        """Create an instance of PeopleResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PeopleResponseDto.parse_obj(obj)

        _obj = PeopleResponseDto.parse_obj({
            "people": [PersonResponseDto.from_dict(_item) for _item in obj.get("people")] if obj.get("people") is not None else None,
            "total": obj.get("total")
        })
        return _obj


