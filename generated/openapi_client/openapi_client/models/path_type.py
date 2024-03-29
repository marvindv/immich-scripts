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





class PathType(str, Enum):
    """
    PathType
    """

    """
    allowed enum values
    """
    ORIGINAL = 'original'
    JPEG_THUMBNAIL = 'jpeg_thumbnail'
    WEBP_THUMBNAIL = 'webp_thumbnail'
    ENCODED_VIDEO = 'encoded_video'
    SIDECAR = 'sidecar'
    FACE = 'face'
    PROFILE = 'profile'

    @classmethod
    def from_json(cls, json_str: str) -> PathType:
        """Create an instance of PathType from a JSON string"""
        return PathType(json.loads(json_str))


