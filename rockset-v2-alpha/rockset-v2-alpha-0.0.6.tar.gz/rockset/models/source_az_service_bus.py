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


class SourceAzServiceBus(object):
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
        'status': 'StatusAzServiceBus',
        'subscription': 'str',
        'topic': 'str'
    }

    attribute_map = {
        'status': 'status',
        'subscription': 'subscription',
        'topic': 'topic'
    }

    def __init__(self, status=None, subscription=None, topic=None, local_vars_configuration=None):  # noqa: E501
        """SourceAzServiceBus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._subscription = None
        self._topic = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if subscription is not None:
            self.subscription = subscription
        if topic is not None:
            self.topic = topic

    @property
    def status(self):
        """Gets the status of this SourceAzServiceBus.  # noqa: E501


        :return: The status of this SourceAzServiceBus.  # noqa: E501
        :rtype: StatusAzServiceBus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SourceAzServiceBus.


        :param status: The status of this SourceAzServiceBus.  # noqa: E501
        :type status: StatusAzServiceBus
        """

        self._status = status

    @property
    def subscription(self):
        """Gets the subscription of this SourceAzServiceBus.  # noqa: E501

        the subscription to read from the topic  # noqa: E501

        :return: The subscription of this SourceAzServiceBus.  # noqa: E501
        :rtype: str
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this SourceAzServiceBus.

        the subscription to read from the topic  # noqa: E501

        :param subscription: The subscription of this SourceAzServiceBus.  # noqa: E501
        :type subscription: str
        """

        self._subscription = subscription

    @property
    def topic(self):
        """Gets the topic of this SourceAzServiceBus.  # noqa: E501

        name of the topic which rockset should ingest from  # noqa: E501

        :return: The topic of this SourceAzServiceBus.  # noqa: E501
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this SourceAzServiceBus.

        name of the topic which rockset should ingest from  # noqa: E501

        :param topic: The topic of this SourceAzServiceBus.  # noqa: E501
        :type topic: str
        """

        self._topic = topic

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
        if not isinstance(other, SourceAzServiceBus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SourceAzServiceBus):
            return True

        return self.to_dict() != other.to_dict()
