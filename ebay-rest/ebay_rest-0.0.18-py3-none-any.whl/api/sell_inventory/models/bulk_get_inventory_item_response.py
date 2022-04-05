# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.16.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BulkGetInventoryItemResponse(object):
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
        'responses': 'list[GetInventoryItemResponse]'
    }

    attribute_map = {
        'responses': 'responses'
    }

    def __init__(self, responses=None):  # noqa: E501
        """BulkGetInventoryItemResponse - a model defined in Swagger"""  # noqa: E501
        self._responses = None
        self.discriminator = None
        if responses is not None:
            self.responses = responses

    @property
    def responses(self):
        """Gets the responses of this BulkGetInventoryItemResponse.  # noqa: E501

        This is the base container of the <strong>bulkGetInventoryItem</strong> response. The results of each attempted inventory item retrieval is captured under this container.  # noqa: E501

        :return: The responses of this BulkGetInventoryItemResponse.  # noqa: E501
        :rtype: list[GetInventoryItemResponse]
        """
        return self._responses

    @responses.setter
    def responses(self, responses):
        """Sets the responses of this BulkGetInventoryItemResponse.

        This is the base container of the <strong>bulkGetInventoryItem</strong> response. The results of each attempted inventory item retrieval is captured under this container.  # noqa: E501

        :param responses: The responses of this BulkGetInventoryItemResponse.  # noqa: E501
        :type: list[GetInventoryItemResponse]
        """

        self._responses = responses

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
        if issubclass(BulkGetInventoryItemResponse, dict):
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
        if not isinstance(other, BulkGetInventoryItemResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
