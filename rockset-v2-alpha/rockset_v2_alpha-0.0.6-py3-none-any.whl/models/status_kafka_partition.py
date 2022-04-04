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


class StatusKafkaPartition(object):
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
        'offset_lag': 'int',
        'partition_number': 'int',
        'partition_offset': 'int'
    }

    attribute_map = {
        'offset_lag': 'offset_lag',
        'partition_number': 'partition_number',
        'partition_offset': 'partition_offset'
    }

    def __init__(self, offset_lag=None, partition_number=None, partition_offset=None, local_vars_configuration=None):  # noqa: E501
        """StatusKafkaPartition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._offset_lag = None
        self._partition_number = None
        self._partition_offset = None
        self.discriminator = None

        if offset_lag is not None:
            self.offset_lag = offset_lag
        if partition_number is not None:
            self.partition_number = partition_number
        if partition_offset is not None:
            self.partition_offset = partition_offset

    @property
    def offset_lag(self):
        """Gets the offset_lag of this StatusKafkaPartition.  # noqa: E501

        Per partition lag for offset  # noqa: E501

        :return: The offset_lag of this StatusKafkaPartition.  # noqa: E501
        :rtype: int
        """
        return self._offset_lag

    @offset_lag.setter
    def offset_lag(self, offset_lag):
        """Sets the offset_lag of this StatusKafkaPartition.

        Per partition lag for offset  # noqa: E501

        :param offset_lag: The offset_lag of this StatusKafkaPartition.  # noqa: E501
        :type offset_lag: int
        """

        self._offset_lag = offset_lag

    @property
    def partition_number(self):
        """Gets the partition_number of this StatusKafkaPartition.  # noqa: E501

        The number of this partition  # noqa: E501

        :return: The partition_number of this StatusKafkaPartition.  # noqa: E501
        :rtype: int
        """
        return self._partition_number

    @partition_number.setter
    def partition_number(self, partition_number):
        """Sets the partition_number of this StatusKafkaPartition.

        The number of this partition  # noqa: E501

        :param partition_number: The partition_number of this StatusKafkaPartition.  # noqa: E501
        :type partition_number: int
        """

        self._partition_number = partition_number

    @property
    def partition_offset(self):
        """Gets the partition_offset of this StatusKafkaPartition.  # noqa: E501

        Latest offset of partition  # noqa: E501

        :return: The partition_offset of this StatusKafkaPartition.  # noqa: E501
        :rtype: int
        """
        return self._partition_offset

    @partition_offset.setter
    def partition_offset(self, partition_offset):
        """Sets the partition_offset of this StatusKafkaPartition.

        Latest offset of partition  # noqa: E501

        :param partition_offset: The partition_offset of this StatusKafkaPartition.  # noqa: E501
        :type partition_offset: int
        """

        self._partition_offset = partition_offset

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
        if not isinstance(other, StatusKafkaPartition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatusKafkaPartition):
            return True

        return self.to_dict() != other.to_dict()
