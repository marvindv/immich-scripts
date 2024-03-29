# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.94.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.system_config_library_watch_dto import SystemConfigLibraryWatchDto  # noqa: E501

class TestSystemConfigLibraryWatchDto(unittest.TestCase):
    """SystemConfigLibraryWatchDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SystemConfigLibraryWatchDto:
        """Test SystemConfigLibraryWatchDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SystemConfigLibraryWatchDto`
        """
        model = SystemConfigLibraryWatchDto()  # noqa: E501
        if include_optional:
            return SystemConfigLibraryWatchDto(
                enabled = True,
                interval = 56,
                use_polling = True
            )
        else:
            return SystemConfigLibraryWatchDto(
                enabled = True,
                interval = 56,
                use_polling = True,
        )
        """

    def testSystemConfigLibraryWatchDto(self):
        """Test SystemConfigLibraryWatchDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
