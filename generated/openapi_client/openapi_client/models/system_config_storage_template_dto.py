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



from pydantic import BaseModel, Field, StrictBool, StrictStr

class SystemConfigStorageTemplateDto(BaseModel):
    """
    SystemConfigStorageTemplateDto
    """
    enabled: StrictBool = Field(...)
    hash_verification_enabled: StrictBool = Field(..., alias="hashVerificationEnabled")
    template: StrictStr = Field(...)
    __properties = ["enabled", "hashVerificationEnabled", "template"]

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
    def from_json(cls, json_str: str) -> SystemConfigStorageTemplateDto:
        """Create an instance of SystemConfigStorageTemplateDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SystemConfigStorageTemplateDto:
        """Create an instance of SystemConfigStorageTemplateDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SystemConfigStorageTemplateDto.parse_obj(obj)

        _obj = SystemConfigStorageTemplateDto.parse_obj({
            "enabled": obj.get("enabled"),
            "hash_verification_enabled": obj.get("hashVerificationEnabled"),
            "template": obj.get("template")
        })
        return _obj


