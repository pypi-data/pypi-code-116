# coding: utf-8

"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from rockset.configuration import Configuration


class GcpServiceAccount(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'service_account_key_file_json': 'str'
    }

    attribute_map = {
        'service_account_key_file_json': 'service_account_key_file_json'
    }

    def __init__(self, service_account_key_file_json=None, local_vars_configuration=None):  # noqa: E501
        """GcpServiceAccount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._service_account_key_file_json = None
        self.discriminator = None

        self.service_account_key_file_json = service_account_key_file_json

    @property
    def service_account_key_file_json(self):
        """Gets the service_account_key_file_json of this GcpServiceAccount.  # noqa: E501

        Contents of JSON Service Account key file  # noqa: E501

        :return: The service_account_key_file_json of this GcpServiceAccount.  # noqa: E501
        :rtype: str
        """
        return self._service_account_key_file_json

    @service_account_key_file_json.setter
    def service_account_key_file_json(self, service_account_key_file_json):
        """Sets the service_account_key_file_json of this GcpServiceAccount.

        Contents of JSON Service Account key file  # noqa: E501

        :param service_account_key_file_json: The service_account_key_file_json of this GcpServiceAccount.  # noqa: E501
        :type service_account_key_file_json: str
        """
        if self.local_vars_configuration.client_side_validation and service_account_key_file_json is None:  # noqa: E501
            raise ValueError("Invalid value for `service_account_key_file_json`, must not be `None`")  # noqa: E501

        self._service_account_key_file_json = service_account_key_file_json

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GcpServiceAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GcpServiceAccount):
            return True

        return self.to_dict() != other.to_dict()
