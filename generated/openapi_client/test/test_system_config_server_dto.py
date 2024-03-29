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

from openapi_client.models.system_config_server_dto import SystemConfigServerDto  # noqa: E501

class TestSystemConfigServerDto(unittest.TestCase):
    """SystemConfigServerDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SystemConfigServerDto:
        """Test SystemConfigServerDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SystemConfigServerDto`
        """
        model = SystemConfigServerDto()  # noqa: E501
        if include_optional:
            return SystemConfigServerDto(
                external_domain = '',
                login_page_message = ''
            )
        else:
            return SystemConfigServerDto(
                external_domain = '',
                login_page_message = '',
        )
        """

    def testSystemConfigServerDto(self):
        """Test SystemConfigServerDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
