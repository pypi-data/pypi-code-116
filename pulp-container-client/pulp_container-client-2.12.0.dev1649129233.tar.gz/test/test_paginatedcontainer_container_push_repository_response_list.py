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
import datetime

import pulpcore.client.pulp_container
from pulpcore.client.pulp_container.models.paginatedcontainer_container_push_repository_response_list import PaginatedcontainerContainerPushRepositoryResponseList  # noqa: E501
from pulpcore.client.pulp_container.rest import ApiException

class TestPaginatedcontainerContainerPushRepositoryResponseList(unittest.TestCase):
    """PaginatedcontainerContainerPushRepositoryResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedcontainerContainerPushRepositoryResponseList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_container.models.paginatedcontainer_container_push_repository_response_list.PaginatedcontainerContainerPushRepositoryResponseList()  # noqa: E501
        if include_optional :
            return PaginatedcontainerContainerPushRepositoryResponseList(
                count = 123, 
                next = 'http://api.example.org/accounts/?offset=400&limit=100', 
                previous = 'http://api.example.org/accounts/?offset=200&limit=100', 
                results = [
                    pulpcore.client.pulp_container.models.container/container_push_repository_response.container.ContainerPushRepositoryResponse(
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        versions_href = '0', 
                        manifest_signing_service = '0', 
                        latest_version_href = '0', 
                        pulp_labels = pulpcore.client.pulp_container.models.pulp_labels.pulp_labels(), 
                        description = '0', 
                        pulp_href = '0', 
                        retain_repo_versions = 1, 
                        name = '0', )
                    ]
            )
        else :
            return PaginatedcontainerContainerPushRepositoryResponseList(
        )

    def testPaginatedcontainerContainerPushRepositoryResponseList(self):
        """Test PaginatedcontainerContainerPushRepositoryResponseList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
