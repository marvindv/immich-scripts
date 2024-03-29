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

class LoginResponseDto(BaseModel):
    """
    LoginResponseDto
    """
    access_token: StrictStr = Field(..., alias="accessToken")
    is_admin: StrictBool = Field(..., alias="isAdmin")
    name: StrictStr = Field(...)
    profile_image_path: StrictStr = Field(..., alias="profileImagePath")
    should_change_password: StrictBool = Field(..., alias="shouldChangePassword")
    user_email: StrictStr = Field(..., alias="userEmail")
    user_id: StrictStr = Field(..., alias="userId")
    __properties = ["accessToken", "isAdmin", "name", "profileImagePath", "shouldChangePassword", "userEmail", "userId"]

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
    def from_json(cls, json_str: str) -> LoginResponseDto:
        """Create an instance of LoginResponseDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoginResponseDto:
        """Create an instance of LoginResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoginResponseDto.parse_obj(obj)

        _obj = LoginResponseDto.parse_obj({
            "access_token": obj.get("accessToken"),
            "is_admin": obj.get("isAdmin"),
            "name": obj.get("name"),
            "profile_image_path": obj.get("profileImagePath"),
            "should_change_password": obj.get("shouldChangePassword"),
            "user_email": obj.get("userEmail"),
            "user_id": obj.get("userId")
        })
        return _obj


