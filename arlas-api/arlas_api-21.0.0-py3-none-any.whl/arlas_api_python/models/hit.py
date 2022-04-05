# coding: utf-8

"""
    ARLAS Exploration API

    Explore the content of ARLAS collections  # noqa: E501

    OpenAPI spec version: 21.0.0
    Contact: contact@gisaia.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Hit(object):
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
        'md': 'MD',
        'data': 'object'
    }

    attribute_map = {
        'md': 'md',
        'data': 'data'
    }

    def __init__(self, md=None, data=None):  # noqa: E501
        """Hit - a model defined in Swagger"""  # noqa: E501

        self._md = None
        self._data = None
        self.discriminator = None

        if md is not None:
            self.md = md
        if data is not None:
            self.data = data

    @property
    def md(self):
        """Gets the md of this Hit.  # noqa: E501


        :return: The md of this Hit.  # noqa: E501
        :rtype: MD
        """
        return self._md

    @md.setter
    def md(self, md):
        """Sets the md of this Hit.


        :param md: The md of this Hit.  # noqa: E501
        :type: MD
        """

        self._md = md

    @property
    def data(self):
        """Gets the data of this Hit.  # noqa: E501


        :return: The data of this Hit.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Hit.


        :param data: The data of this Hit.  # noqa: E501
        :type: object
        """

        self._data = data

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
        if issubclass(Hit, dict):
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
        if not isinstance(other, Hit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
