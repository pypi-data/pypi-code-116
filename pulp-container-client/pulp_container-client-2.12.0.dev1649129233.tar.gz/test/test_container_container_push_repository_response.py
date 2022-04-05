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
from pulpcore.client.pulp_container.models.container_container_push_repository_response import ContainerContainerPushRepositoryResponse  # noqa: E501
from pulpcore.client.pulp_container.rest import ApiException

class TestContainerContainerPushRepositoryResponse(unittest.TestCase):
    """ContainerContainerPushRepositoryResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ContainerContainerPushRepositoryResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_container.models.container_container_push_repository_response.ContainerContainerPushRepositoryResponse()  # noqa: E501
        if include_optional :
            return ContainerContainerPushRepositoryResponse(
                pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                versions_href = '0', 
                manifest_signing_service = '0', 
                latest_version_href = '0', 
                pulp_labels = pulpcore.client.pulp_container.models.pulp_labels.pulp_labels(), 
                description = '0', 
                pulp_href = '0', 
                retain_repo_versions = 1, 
                name = '0'
            )
        else :
            return ContainerContainerPushRepositoryResponse(
                name = '0',
        )

    def testContainerContainerPushRepositoryResponse(self):
        """Test ContainerContainerPushRepositoryResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
