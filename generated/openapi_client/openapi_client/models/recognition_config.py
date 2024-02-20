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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from openapi_client.models.model_type import ModelType

class RecognitionConfig(BaseModel):
    """
    RecognitionConfig
    """
    enabled: StrictBool = Field(...)
    max_distance: Union[StrictFloat, StrictInt] = Field(..., alias="maxDistance")
    min_faces: StrictInt = Field(..., alias="minFaces")
    min_score: Union[StrictFloat, StrictInt] = Field(..., alias="minScore")
    model_name: StrictStr = Field(..., alias="modelName")
    model_type: Optional[ModelType] = Field(None, alias="modelType")
    __properties = ["enabled", "maxDistance", "minFaces", "minScore", "modelName", "modelType"]

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
    def from_json(cls, json_str: str) -> RecognitionConfig:
        """Create an instance of RecognitionConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RecognitionConfig:
        """Create an instance of RecognitionConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RecognitionConfig.parse_obj(obj)

        _obj = RecognitionConfig.parse_obj({
            "enabled": obj.get("enabled"),
            "max_distance": obj.get("maxDistance"),
            "min_faces": obj.get("minFaces"),
            "min_score": obj.get("minScore"),
            "model_name": obj.get("modelName"),
            "model_type": obj.get("modelType")
        })
        return _obj

