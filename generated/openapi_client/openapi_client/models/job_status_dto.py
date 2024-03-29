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



from pydantic import BaseModel, Field
from openapi_client.models.job_counts_dto import JobCountsDto
from openapi_client.models.queue_status_dto import QueueStatusDto

class JobStatusDto(BaseModel):
    """
    JobStatusDto
    """
    job_counts: JobCountsDto = Field(..., alias="jobCounts")
    queue_status: QueueStatusDto = Field(..., alias="queueStatus")
    __properties = ["jobCounts", "queueStatus"]

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
    def from_json(cls, json_str: str) -> JobStatusDto:
        """Create an instance of JobStatusDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of job_counts
        if self.job_counts:
            _dict['jobCounts'] = self.job_counts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of queue_status
        if self.queue_status:
            _dict['queueStatus'] = self.queue_status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JobStatusDto:
        """Create an instance of JobStatusDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return JobStatusDto.parse_obj(obj)

        _obj = JobStatusDto.parse_obj({
            "job_counts": JobCountsDto.from_dict(obj.get("jobCounts")) if obj.get("jobCounts") is not None else None,
            "queue_status": QueueStatusDto.from_dict(obj.get("queueStatus")) if obj.get("queueStatus") is not None else None
        })
        return _obj


