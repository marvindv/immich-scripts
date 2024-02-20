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





class SharedLinkType(str, Enum):
    """
    SharedLinkType
    """

    """
    allowed enum values
    """
    ALBUM = 'ALBUM'
    INDIVIDUAL = 'INDIVIDUAL'

    @classmethod
    def from_json(cls, json_str: str) -> SharedLinkType:
        """Create an instance of SharedLinkType from a JSON string"""
        return SharedLinkType(json.loads(json_str))


