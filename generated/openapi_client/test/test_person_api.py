# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.79.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.person_api import PersonApi  # noqa: E501


class TestPersonApi(unittest.TestCase):
    """PersonApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PersonApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_get_all_people(self) -> None:
        """Test case for get_all_people

        """
        pass

    def test_get_person(self) -> None:
        """Test case for get_person

        """
        pass

    def test_get_person_assets(self) -> None:
        """Test case for get_person_assets

        """
        pass

    def test_get_person_thumbnail(self) -> None:
        """Test case for get_person_thumbnail

        """
        pass

    def test_merge_person(self) -> None:
        """Test case for merge_person

        """
        pass

    def test_update_people(self) -> None:
        """Test case for update_people

        """
        pass

    def test_update_person(self) -> None:
        """Test case for update_person

        """
        pass


if __name__ == '__main__':
    unittest.main()
