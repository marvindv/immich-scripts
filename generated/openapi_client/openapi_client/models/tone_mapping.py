# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.94.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ToneMapping(str, Enum):
    """
    ToneMapping
    """

    """
    allowed enum values
    """
    HABLE = 'hable'
    MOBIUS = 'mobius'
    REINHARD = 'reinhard'
    DISABLED = 'disabled'

    @classmethod
    def from_json(cls, json_str: str) -> ToneMapping:
        """Create an instance of ToneMapping from a JSON string"""
        return ToneMapping(json.loads(json_str))


