# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pulpcore.client.pulp_container
from pulpcore.client.pulp_container.api.distributions_container_api import DistributionsContainerApi  # noqa: E501
from pulpcore.client.pulp_container.rest import ApiException


class TestDistributionsContainerApi(unittest.TestCase):
    """DistributionsContainerApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_container.api.distributions_container_api.DistributionsContainerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_role(self):
        """Test case for add_role

        """
        pass

    def test_create(self):
        """Test case for create

        Create a container distribution  # noqa: E501
        """
        pass

    def test_delete(self):
        """Test case for delete

        Delete a container distribution  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List container distributions  # noqa: E501
        """
        pass

    def test_list_roles(self):
        """Test case for list_roles

        """
        pass

    def test_my_permissions(self):
        """Test case for my_permissions

        """
        pass

    def test_partial_update(self):
        """Test case for partial_update

        Update a container distribution  # noqa: E501
        """
        pass

    def test_read(self):
        """Test case for read

        Inspect a container distribution  # noqa: E501
        """
        pass

    def test_remove_role(self):
        """Test case for remove_role

        """
        pass

    def test_update(self):
        """Test case for update

        Update a container distribution  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
