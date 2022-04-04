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


class VirtualInstance(object):
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
        'current_size': 'str',
        'current_type': 'str',
        'default_pod_count': 'int',
        'desired_size': 'str',
        'desired_type': 'str',
        'estimated_switch_duration_minutes': 'int',
        'id': 'str',
        'last_updated': 'str',
        'monitoring_enabled': 'bool',
        'scaled_pod_count': 'int',
        'state': 'str'
    }

    attribute_map = {
        'current_size': 'current_size',
        'current_type': 'current_type',
        'default_pod_count': 'default_pod_count',
        'desired_size': 'desired_size',
        'desired_type': 'desired_type',
        'estimated_switch_duration_minutes': 'estimated_switch_duration_minutes',
        'id': 'id',
        'last_updated': 'last_updated',
        'monitoring_enabled': 'monitoring_enabled',
        'scaled_pod_count': 'scaled_pod_count',
        'state': 'state'
    }

    def __init__(self, current_size=None, current_type=None, default_pod_count=None, desired_size=None, desired_type=None, estimated_switch_duration_minutes=None, id=None, last_updated=None, monitoring_enabled=None, scaled_pod_count=None, state=None, local_vars_configuration=None):  # noqa: E501
        """VirtualInstance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._current_size = None
        self._current_type = None
        self._default_pod_count = None
        self._desired_size = None
        self._desired_type = None
        self._estimated_switch_duration_minutes = None
        self._id = None
        self._last_updated = None
        self._monitoring_enabled = None
        self._scaled_pod_count = None
        self._state = None
        self.discriminator = None

        if current_size is not None:
            self.current_size = current_size
        if current_type is not None:
            self.current_type = current_type
        if default_pod_count is not None:
            self.default_pod_count = default_pod_count
        if desired_size is not None:
            self.desired_size = desired_size
        if desired_type is not None:
            self.desired_type = desired_type
        if estimated_switch_duration_minutes is not None:
            self.estimated_switch_duration_minutes = estimated_switch_duration_minutes
        if id is not None:
            self.id = id
        if last_updated is not None:
            self.last_updated = last_updated
        if monitoring_enabled is not None:
            self.monitoring_enabled = monitoring_enabled
        if scaled_pod_count is not None:
            self.scaled_pod_count = scaled_pod_count
        if state is not None:
            self.state = state

    @property
    def current_size(self):
        """Gets the current_size of this VirtualInstance.  # noqa: E501

        virtual instance current size  # noqa: E501

        :return: The current_size of this VirtualInstance.  # noqa: E501
        :rtype: str
        """
        return self._current_size

    @current_size.setter
    def current_size(self, current_size):
        """Sets the current_size of this VirtualInstance.

        virtual instance current size  # noqa: E501

        :param current_size: The current_size of this VirtualInstance.  # noqa: E501
        :type current_size: str
        """
        allowed_values = ["FREE", "SHARED", "SMALL", "MEDIUM", "LARGE", "XLARGE", "XLARGE2", "XLARGE4", "XLARGE8", "XLARGE16"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and current_size not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `current_size` ({0}), must be one of {1}"  # noqa: E501
                .format(current_size, allowed_values)
            )

        self._current_size = current_size

    @property
    def current_type(self):
        """Gets the current_type of this VirtualInstance.  # noqa: E501


        :return: The current_type of this VirtualInstance.  # noqa: E501
        :rtype: str
        """
        return self._current_type

    @current_type.setter
    def current_type(self, current_type):
        """Sets the current_type of this VirtualInstance.


        :param current_type: The current_type of this VirtualInstance.  # noqa: E501
        :type current_type: str
        """
        allowed_values = ["FREE", "SHARED", "SMALL", "MEDIUM", "LARGE", "XLARGE", "XLARGE2", "XLARGE4", "XLARGE8", "XLARGE16"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and current_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `current_type` ({0}), must be one of {1}"  # noqa: E501
                .format(current_type, allowed_values)
            )

        self._current_type = current_type

    @property
    def default_pod_count(self):
        """Gets the default_pod_count of this VirtualInstance.  # noqa: E501


        :return: The default_pod_count of this VirtualInstance.  # noqa: E501
        :rtype: int
        """
        return self._default_pod_count

    @default_pod_count.setter
    def default_pod_count(self, default_pod_count):
        """Sets the default_pod_count of this VirtualInstance.


        :param default_pod_count: The default_pod_count of this VirtualInstance.  # noqa: E501
        :type default_pod_count: int
        """

        self._default_pod_count = default_pod_count

    @property
    def desired_size(self):
        """Gets the desired_size of this VirtualInstance.  # noqa: E501

        virtual instance desired size  # noqa: E501

        :return: The desired_size of this VirtualInstance.  # noqa: E501
        :rtype: str
        """
        return self._desired_size

    @desired_size.setter
    def desired_size(self, desired_size):
        """Sets the desired_size of this VirtualInstance.

        virtual instance desired size  # noqa: E501

        :param desired_size: The desired_size of this VirtualInstance.  # noqa: E501
        :type desired_size: str
        """
        allowed_values = ["FREE", "SHARED", "SMALL", "MEDIUM", "LARGE", "XLARGE", "XLARGE2", "XLARGE4", "XLARGE8", "XLARGE16"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and desired_size not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `desired_size` ({0}), must be one of {1}"  # noqa: E501
                .format(desired_size, allowed_values)
            )

        self._desired_size = desired_size

    @property
    def desired_type(self):
        """Gets the desired_type of this VirtualInstance.  # noqa: E501


        :return: The desired_type of this VirtualInstance.  # noqa: E501
        :rtype: str
        """
        return self._desired_type

    @desired_type.setter
    def desired_type(self, desired_type):
        """Sets the desired_type of this VirtualInstance.


        :param desired_type: The desired_type of this VirtualInstance.  # noqa: E501
        :type desired_type: str
        """
        allowed_values = ["FREE", "SHARED", "SMALL", "MEDIUM", "LARGE", "XLARGE", "XLARGE2", "XLARGE4", "XLARGE8", "XLARGE16"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and desired_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `desired_type` ({0}), must be one of {1}"  # noqa: E501
                .format(desired_type, allowed_values)
            )

        self._desired_type = desired_type

    @property
    def estimated_switch_duration_minutes(self):
        """Gets the estimated_switch_duration_minutes of this VirtualInstance.  # noqa: E501

        estimated duration in minutes of last virtual instance size update  # noqa: E501

        :return: The estimated_switch_duration_minutes of this VirtualInstance.  # noqa: E501
        :rtype: int
        """
        return self._estimated_switch_duration_minutes

    @estimated_switch_duration_minutes.setter
    def estimated_switch_duration_minutes(self, estimated_switch_duration_minutes):
        """Sets the estimated_switch_duration_minutes of this VirtualInstance.

        estimated duration in minutes of last virtual instance size update  # noqa: E501

        :param estimated_switch_duration_minutes: The estimated_switch_duration_minutes of this VirtualInstance.  # noqa: E501
        :type estimated_switch_duration_minutes: int
        """

        self._estimated_switch_duration_minutes = estimated_switch_duration_minutes

    @property
    def id(self):
        """Gets the id of this VirtualInstance.  # noqa: E501

        unique identifier for virtual instance  # noqa: E501

        :return: The id of this VirtualInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VirtualInstance.

        unique identifier for virtual instance  # noqa: E501

        :param id: The id of this VirtualInstance.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def last_updated(self):
        """Gets the last_updated of this VirtualInstance.  # noqa: E501

        ISO-8601 date of when virtual instance size was last updated  # noqa: E501

        :return: The last_updated of this VirtualInstance.  # noqa: E501
        :rtype: str
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this VirtualInstance.

        ISO-8601 date of when virtual instance size was last updated  # noqa: E501

        :param last_updated: The last_updated of this VirtualInstance.  # noqa: E501
        :type last_updated: str
        """

        self._last_updated = last_updated

    @property
    def monitoring_enabled(self):
        """Gets the monitoring_enabled of this VirtualInstance.  # noqa: E501


        :return: The monitoring_enabled of this VirtualInstance.  # noqa: E501
        :rtype: bool
        """
        return self._monitoring_enabled

    @monitoring_enabled.setter
    def monitoring_enabled(self, monitoring_enabled):
        """Sets the monitoring_enabled of this VirtualInstance.


        :param monitoring_enabled: The monitoring_enabled of this VirtualInstance.  # noqa: E501
        :type monitoring_enabled: bool
        """

        self._monitoring_enabled = monitoring_enabled

    @property
    def scaled_pod_count(self):
        """Gets the scaled_pod_count of this VirtualInstance.  # noqa: E501


        :return: The scaled_pod_count of this VirtualInstance.  # noqa: E501
        :rtype: int
        """
        return self._scaled_pod_count

    @scaled_pod_count.setter
    def scaled_pod_count(self, scaled_pod_count):
        """Sets the scaled_pod_count of this VirtualInstance.


        :param scaled_pod_count: The scaled_pod_count of this VirtualInstance.  # noqa: E501
        :type scaled_pod_count: int
        """

        self._scaled_pod_count = scaled_pod_count

    @property
    def state(self):
        """Gets the state of this VirtualInstance.  # noqa: E501

        virtual instance state  # noqa: E501

        :return: The state of this VirtualInstance.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this VirtualInstance.

        virtual instance state  # noqa: E501

        :param state: The state of this VirtualInstance.  # noqa: E501
        :type state: str
        """
        allowed_values = ["PROVISIONING_RESOURCES", "REBALANCING_COLLECTIONS", "ACTIVE", "DELETED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

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
        if not isinstance(other, VirtualInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VirtualInstance):
            return True

        return self.to_dict() != other.to_dict()
