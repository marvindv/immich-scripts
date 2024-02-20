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

from openapi_client.models.memory_lane_response_dto import MemoryLaneResponseDto  # noqa: E501

class TestMemoryLaneResponseDto(unittest.TestCase):
    """MemoryLaneResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MemoryLaneResponseDto:
        """Test MemoryLaneResponseDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MemoryLaneResponseDto`
        """
        model = MemoryLaneResponseDto()  # noqa: E501
        if include_optional:
            return MemoryLaneResponseDto(
                assets = [
                    openapi_client.models.asset_response_dto.AssetResponseDto(
                        checksum = '', 
                        device_asset_id = '', 
                        device_id = '', 
                        duration = '', 
                        exif_info = openapi_client.models.exif_response_dto.ExifResponseDto(
                            city = '', 
                            country = '', 
                            date_time_original = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            description = '', 
                            exif_image_height = 1.337, 
                            exif_image_width = 1.337, 
                            exposure_time = '', 
                            f_number = 1.337, 
                            file_size_in_byte = 56, 
                            focal_length = 1.337, 
                            iso = 1.337, 
                            latitude = 1.337, 
                            lens_model = '', 
                            longitude = 1.337, 
                            make = '', 
                            model = '', 
                            modify_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            orientation = '', 
                            projection_type = '', 
                            state = '', 
                            time_zone = '', ), 
                        file_created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        file_modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        is_archived = True, 
                        is_external = True, 
                        is_favorite = True, 
                        is_offline = True, 
                        is_read_only = True, 
                        library_id = '', 
                        live_photo_video_id = '', 
                        original_file_name = '', 
                        original_path = '', 
                        owner = openapi_client.models.user_response_dto.UserResponseDto(
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            email = '', 
                            external_path = '', 
                            first_name = '', 
                            id = '', 
                            is_admin = True, 
                            last_name = '', 
                            memories_enabled = True, 
                            oauth_id = '', 
                            profile_image_path = '', 
                            should_change_password = True, 
                            storage_label = '', 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        owner_id = '', 
                        people = [
                            openapi_client.models.person_response_dto.PersonResponseDto(
                                birth_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                id = '', 
                                is_hidden = True, 
                                name = '', 
                                thumbnail_path = '', )
                            ], 
                        resized = True, 
                        smart_info = openapi_client.models.smart_info_response_dto.SmartInfoResponseDto(
                            objects = [
                                ''
                                ], 
                            tags = [
                                ''
                                ], ), 
                        tags = [
                            openapi_client.models.tag_response_dto.TagResponseDto(
                                id = '', 
                                name = '', 
                                type = 'OBJECT', 
                                user_id = '', )
                            ], 
                        thumbhash = '', 
                        type = 'IMAGE', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                title = ''
            )
        else:
            return MemoryLaneResponseDto(
                assets = [
                    openapi_client.models.asset_response_dto.AssetResponseDto(
                        checksum = '', 
                        device_asset_id = '', 
                        device_id = '', 
                        duration = '', 
                        exif_info = openapi_client.models.exif_response_dto.ExifResponseDto(
                            city = '', 
                            country = '', 
                            date_time_original = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            description = '', 
                            exif_image_height = 1.337, 
                            exif_image_width = 1.337, 
                            exposure_time = '', 
                            f_number = 1.337, 
                            file_size_in_byte = 56, 
                            focal_length = 1.337, 
                            iso = 1.337, 
                            latitude = 1.337, 
                            lens_model = '', 
                            longitude = 1.337, 
                            make = '', 
                            model = '', 
                            modify_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            orientation = '', 
                            projection_type = '', 
                            state = '', 
                            time_zone = '', ), 
                        file_created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        file_modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        is_archived = True, 
                        is_external = True, 
                        is_favorite = True, 
                        is_offline = True, 
                        is_read_only = True, 
                        library_id = '', 
                        live_photo_video_id = '', 
                        original_file_name = '', 
                        original_path = '', 
                        owner = openapi_client.models.user_response_dto.UserResponseDto(
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            email = '', 
                            external_path = '', 
                            first_name = '', 
                            id = '', 
                            is_admin = True, 
                            last_name = '', 
                            memories_enabled = True, 
                            oauth_id = '', 
                            profile_image_path = '', 
                            should_change_password = True, 
                            storage_label = '', 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        owner_id = '', 
                        people = [
                            openapi_client.models.person_response_dto.PersonResponseDto(
                                birth_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                id = '', 
                                is_hidden = True, 
                                name = '', 
                                thumbnail_path = '', )
                            ], 
                        resized = True, 
                        smart_info = openapi_client.models.smart_info_response_dto.SmartInfoResponseDto(
                            objects = [
                                ''
                                ], 
                            tags = [
                                ''
                                ], ), 
                        tags = [
                            openapi_client.models.tag_response_dto.TagResponseDto(
                                id = '', 
                                name = '', 
                                type = 'OBJECT', 
                                user_id = '', )
                            ], 
                        thumbhash = '', 
                        type = 'IMAGE', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                title = '',
        )
        """

    def testMemoryLaneResponseDto(self):
        """Test MemoryLaneResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
