# coding: utf-8

"""
    Kubeflow Pipelines API

    This file contains REST API specification for Kubeflow Pipelines. The file is autogenerated from the swagger definition.

    Contact: kubeflow-pipelines@google.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kfp_server_api
from kfp_server_api.api.healthz_service_api import HealthzServiceApi  # noqa: E501
from kfp_server_api.rest import ApiException


class TestHealthzServiceApi(unittest.TestCase):
    """HealthzServiceApi unit test stubs"""

    def setUp(self):
        self.api = kfp_server_api.api.healthz_service_api.HealthzServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_healthz(self):
        """Test case for get_healthz

        Get healthz data.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
