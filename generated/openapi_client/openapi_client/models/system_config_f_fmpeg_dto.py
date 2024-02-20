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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from openapi_client.models.audio_codec import AudioCodec
from openapi_client.models.cq_mode import CQMode
from openapi_client.models.tone_mapping import ToneMapping
from openapi_client.models.transcode_hw_accel import TranscodeHWAccel
from openapi_client.models.transcode_policy import TranscodePolicy
from openapi_client.models.video_codec import VideoCodec

class SystemConfigFFmpegDto(BaseModel):
    """
    SystemConfigFFmpegDto
    """
    accel: TranscodeHWAccel = Field(...)
    accepted_audio_codecs: conlist(AudioCodec) = Field(..., alias="acceptedAudioCodecs")
    accepted_video_codecs: conlist(VideoCodec) = Field(..., alias="acceptedVideoCodecs")
    bframes: StrictInt = Field(...)
    cq_mode: CQMode = Field(..., alias="cqMode")
    crf: StrictInt = Field(...)
    gop_size: StrictInt = Field(..., alias="gopSize")
    max_bitrate: StrictStr = Field(..., alias="maxBitrate")
    npl: StrictInt = Field(...)
    preferred_hw_device: StrictStr = Field(..., alias="preferredHwDevice")
    preset: StrictStr = Field(...)
    refs: StrictInt = Field(...)
    target_audio_codec: AudioCodec = Field(..., alias="targetAudioCodec")
    target_resolution: StrictStr = Field(..., alias="targetResolution")
    target_video_codec: VideoCodec = Field(..., alias="targetVideoCodec")
    temporal_aq: StrictBool = Field(..., alias="temporalAQ")
    threads: StrictInt = Field(...)
    tonemap: ToneMapping = Field(...)
    transcode: TranscodePolicy = Field(...)
    two_pass: StrictBool = Field(..., alias="twoPass")
    __properties = ["accel", "acceptedAudioCodecs", "acceptedVideoCodecs", "bframes", "cqMode", "crf", "gopSize", "maxBitrate", "npl", "preferredHwDevice", "preset", "refs", "targetAudioCodec", "targetResolution", "targetVideoCodec", "temporalAQ", "threads", "tonemap", "transcode", "twoPass"]

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
    def from_json(cls, json_str: str) -> SystemConfigFFmpegDto:
        """Create an instance of SystemConfigFFmpegDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SystemConfigFFmpegDto:
        """Create an instance of SystemConfigFFmpegDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SystemConfigFFmpegDto.parse_obj(obj)

        _obj = SystemConfigFFmpegDto.parse_obj({
            "accel": obj.get("accel"),
            "accepted_audio_codecs": obj.get("acceptedAudioCodecs"),
            "accepted_video_codecs": obj.get("acceptedVideoCodecs"),
            "bframes": obj.get("bframes"),
            "cq_mode": obj.get("cqMode"),
            "crf": obj.get("crf"),
            "gop_size": obj.get("gopSize"),
            "max_bitrate": obj.get("maxBitrate"),
            "npl": obj.get("npl"),
            "preferred_hw_device": obj.get("preferredHwDevice"),
            "preset": obj.get("preset"),
            "refs": obj.get("refs"),
            "target_audio_codec": obj.get("targetAudioCodec"),
            "target_resolution": obj.get("targetResolution"),
            "target_video_codec": obj.get("targetVideoCodec"),
            "temporal_aq": obj.get("temporalAQ"),
            "threads": obj.get("threads"),
            "tonemap": obj.get("tonemap"),
            "transcode": obj.get("transcode"),
            "two_pass": obj.get("twoPass")
        })
        return _obj


