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

from openapi_client.models.asset_face_response_dto import AssetFaceResponseDto  # noqa: E501

class TestAssetFaceResponseDto(unittest.TestCase):
    """AssetFaceResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AssetFaceResponseDto:
        """Test AssetFaceResponseDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AssetFaceResponseDto`
        """
        model = AssetFaceResponseDto()  # noqa: E501
        if include_optional:
            return AssetFaceResponseDto(
                bounding_box_x1 = 56,
                bounding_box_x2 = 56,
                bounding_box_y1 = 56,
                bounding_box_y2 = 56,
                id = '',
                image_height = 56,
                image_width = 56,
                person = openapi_client.models.person_response_dto.PersonResponseDto(
                    birth_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    id = '', 
                    is_hidden = True, 
                    name = '', 
                    thumbnail_path = '', )
            )
        else:
            return AssetFaceResponseDto(
                bounding_box_x1 = 56,
                bounding_box_x2 = 56,
                bounding_box_y1 = 56,
                bounding_box_y2 = 56,
                id = '',
                image_height = 56,
                image_width = 56,
                person = openapi_client.models.person_response_dto.PersonResponseDto(
                    birth_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    id = '', 
                    is_hidden = True, 
                    name = '', 
                    thumbnail_path = '', ),
        )
        """

    def testAssetFaceResponseDto(self):
        """Test AssetFaceResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()