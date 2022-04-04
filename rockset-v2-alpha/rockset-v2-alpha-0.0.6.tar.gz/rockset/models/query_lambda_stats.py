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


class QueryLambdaStats(object):
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
        'last_executed': 'str',
        'last_executed_by': 'str',
        'last_execution_error': 'str',
        'last_execution_error_message': 'str'
    }

    attribute_map = {
        'last_executed': 'last_executed',
        'last_executed_by': 'last_executed_by',
        'last_execution_error': 'last_execution_error',
        'last_execution_error_message': 'last_execution_error_message'
    }

    def __init__(self, last_executed=None, last_executed_by=None, last_execution_error=None, last_execution_error_message=None, local_vars_configuration=None):  # noqa: E501
        """QueryLambdaStats - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._last_executed = None
        self._last_executed_by = None
        self._last_execution_error = None
        self._last_execution_error_message = None
        self.discriminator = None

        if last_executed is not None:
            self.last_executed = last_executed
        if last_executed_by is not None:
            self.last_executed_by = last_executed_by
        if last_execution_error is not None:
            self.last_execution_error = last_execution_error
        if last_execution_error_message is not None:
            self.last_execution_error_message = last_execution_error_message

    @property
    def last_executed(self):
        """Gets the last_executed of this QueryLambdaStats.  # noqa: E501

        ISO-8601 date  # noqa: E501

        :return: The last_executed of this QueryLambdaStats.  # noqa: E501
        :rtype: str
        """
        return self._last_executed

    @last_executed.setter
    def last_executed(self, last_executed):
        """Sets the last_executed of this QueryLambdaStats.

        ISO-8601 date  # noqa: E501

        :param last_executed: The last_executed of this QueryLambdaStats.  # noqa: E501
        :type last_executed: str
        """

        self._last_executed = last_executed

    @property
    def last_executed_by(self):
        """Gets the last_executed_by of this QueryLambdaStats.  # noqa: E501

        user who last executed Query Lambda  # noqa: E501

        :return: The last_executed_by of this QueryLambdaStats.  # noqa: E501
        :rtype: str
        """
        return self._last_executed_by

    @last_executed_by.setter
    def last_executed_by(self, last_executed_by):
        """Sets the last_executed_by of this QueryLambdaStats.

        user who last executed Query Lambda  # noqa: E501

        :param last_executed_by: The last_executed_by of this QueryLambdaStats.  # noqa: E501
        :type last_executed_by: str
        """

        self._last_executed_by = last_executed_by

    @property
    def last_execution_error(self):
        """Gets the last_execution_error of this QueryLambdaStats.  # noqa: E501

        ISO-8601 date of last execution failure  # noqa: E501

        :return: The last_execution_error of this QueryLambdaStats.  # noqa: E501
        :rtype: str
        """
        return self._last_execution_error

    @last_execution_error.setter
    def last_execution_error(self, last_execution_error):
        """Sets the last_execution_error of this QueryLambdaStats.

        ISO-8601 date of last execution failure  # noqa: E501

        :param last_execution_error: The last_execution_error of this QueryLambdaStats.  # noqa: E501
        :type last_execution_error: str
        """

        self._last_execution_error = last_execution_error

    @property
    def last_execution_error_message(self):
        """Gets the last_execution_error_message of this QueryLambdaStats.  # noqa: E501

        error message associated with last failed execution  # noqa: E501

        :return: The last_execution_error_message of this QueryLambdaStats.  # noqa: E501
        :rtype: str
        """
        return self._last_execution_error_message

    @last_execution_error_message.setter
    def last_execution_error_message(self, last_execution_error_message):
        """Sets the last_execution_error_message of this QueryLambdaStats.

        error message associated with last failed execution  # noqa: E501

        :param last_execution_error_message: The last_execution_error_message of this QueryLambdaStats.  # noqa: E501
        :type last_execution_error_message: str
        """

        self._last_execution_error_message = last_execution_error_message

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
        if not isinstance(other, QueryLambdaStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryLambdaStats):
            return True

        return self.to_dict() != other.to_dict()
