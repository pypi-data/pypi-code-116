# coding: utf-8

"""
    eBay Finances API

    This API is used to retrieve seller payouts and monetary transaction details related to those payouts.  # noqa: E501

    OpenAPI spec version: v1.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Buyer(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'username': 'str'
    }

    attribute_map = {
        'username': 'username'
    }

    def __init__(self, username=None):  # noqa: E501
        """Buyer - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self.discriminator = None
        if username is not None:
            self.username = username

    @property
    def username(self):
        """Gets the username of this Buyer.  # noqa: E501

        The eBay user ID of the order's buyer.  # noqa: E501

        :return: The username of this Buyer.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Buyer.

        The eBay user ID of the order's buyer.  # noqa: E501

        :param username: The username of this Buyer.  # noqa: E501
        :type: str
        """

        self._username = username

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Buyer, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Buyer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
