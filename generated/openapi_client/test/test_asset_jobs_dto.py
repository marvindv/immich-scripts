# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.79.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.asset_jobs_dto import AssetJobsDto  # noqa: E501

class TestAssetJobsDto(unittest.TestCase):
    """AssetJobsDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AssetJobsDto:
        """Test AssetJobsDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AssetJobsDto`
        """
        model = AssetJobsDto()  # noqa: E501
        if include_optional:
            return AssetJobsDto(
                asset_ids = [
                    ''
                    ],
                name = 'regenerate-thumbnail'
            )
        else:
            return AssetJobsDto(
                asset_ids = [
                    ''
                    ],
                name = 'regenerate-thumbnail',
        )
        """

    def testAssetJobsDto(self):
        """Test AssetJobsDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
