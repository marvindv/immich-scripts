# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.94.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.trash_api import TrashApi  # noqa: E501


class TestTrashApi(unittest.TestCase):
    """TrashApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TrashApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_empty_trash(self) -> None:
        """Test case for empty_trash

        """
        pass

    def test_restore_assets(self) -> None:
        """Test case for restore_assets

        """
        pass

    def test_restore_trash(self) -> None:
        """Test case for restore_trash

        """
        pass


if __name__ == '__main__':
    unittest.main()