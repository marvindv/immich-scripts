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





class AssetOrder(str, Enum):
    """
    AssetOrder
    """

    """
    allowed enum values
    """
    ASC = 'asc'
    DESC = 'desc'

    @classmethod
    def from_json(cls, json_str: str) -> AssetOrder:
        """Create an instance of AssetOrder from a JSON string"""
        return AssetOrder(json.loads(json_str))


