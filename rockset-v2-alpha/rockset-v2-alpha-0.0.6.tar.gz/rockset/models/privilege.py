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


class Privilege(object):
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
        'action': 'str',
        'cluster': 'str',
        'resource_name': 'str'
    }

    attribute_map = {
        'action': 'action',
        'cluster': 'cluster',
        'resource_name': 'resource_name'
    }

    def __init__(self, action=None, cluster=None, resource_name=None, local_vars_configuration=None):  # noqa: E501
        """Privilege - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._action = None
        self._cluster = None
        self._resource_name = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if cluster is not None:
            self.cluster = cluster
        if resource_name is not None:
            self.resource_name = resource_name

    @property
    def action(self):
        """Gets the action of this Privilege.  # noqa: E501

        The action allowed by this privilege.  # noqa: E501

        :return: The action of this Privilege.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this Privilege.

        The action allowed by this privilege.  # noqa: E501

        :param action: The action of this Privilege.  # noqa: E501
        :type action: str
        """
        allowed_values = ["ALL_GLOBAL_ACTIONS", "GET_ORG_GLOBAL", "GET_CURRENT_USER_GLOBAL", "INVITE_USER_GLOBAL", "DELETE_USER_GLOBAL", "LIST_USERS_GLOBAL", "GET_BILLING_GLOBAL", "UPDATE_BILLING_GLOBAL", "UPDATE_SETTINGS_GLOBAL", "GET_METRICS_GLOBAL", "UPDATE_VI_GLOBAL", "LIST_VI_GLOBAL", "CREATE_WS_GLOBAL", "LIST_WS_GLOBAL", "CREATE_INTEGRATION_GLOBAL", "DELETE_INTEGRATION_GLOBAL", "LIST_INTEGRATIONS_GLOBAL", "UPDATE_RESOURCE_OWNER_GLOBAL", "CREATE_API_KEY_GLOBAL", "CREATE_ROLE_GLOBAL", "UPDATE_ROLE_GLOBAL", "DELETE_ROLE_GLOBAL", "LIST_ROLES_GLOBAL", "GRANT_REVOKE_ROLE_GLOBAL", "ALL_INTEGRATION_ACTIONS", "CREATE_COLLECTION_INTEGRATION", "ALL_WORKSPACE_ACTIONS", "DELETE_WS", "QUERY_DATA_WS", "WRITE_DATA_WS", "CREATE_COLLECTION_WS", "DELETE_COLLECTION_WS", "CREATE_ALIAS_WS", "DELETE_ALIAS_WS", "LIST_RESOURCES_WS", "CREATE_QUERY_LAMBDA_WS", "DELETE_QUERY_LAMBDA_WS", "EXECUTE_QUERY_LAMBDA_WS", "CREATE_VIEW_WS", "DELETE_VIEW_WS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and action not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def cluster(self):
        """Gets the cluster of this Privilege.  # noqa: E501

        Cluster ID (`rs2` for us-west-2, `use1a1` for us-east-1) for which the action is allowed. Defaults to '*All*' if not specified.  # noqa: E501

        :return: The cluster of this Privilege.  # noqa: E501
        :rtype: str
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this Privilege.

        Cluster ID (`rs2` for us-west-2, `use1a1` for us-east-1) for which the action is allowed. Defaults to '*All*' if not specified.  # noqa: E501

        :param cluster: The cluster of this Privilege.  # noqa: E501
        :type cluster: str
        """

        self._cluster = cluster

    @property
    def resource_name(self):
        """Gets the resource_name of this Privilege.  # noqa: E501

        The resources on which the action is allowed. Defaults to '*All*' if not specified.  # noqa: E501

        :return: The resource_name of this Privilege.  # noqa: E501
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this Privilege.

        The resources on which the action is allowed. Defaults to '*All*' if not specified.  # noqa: E501

        :param resource_name: The resource_name of this Privilege.  # noqa: E501
        :type resource_name: str
        """

        self._resource_name = resource_name

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
        if not isinstance(other, Privilege):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Privilege):
            return True

        return self.to_dict() != other.to_dict()
