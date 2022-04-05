# coding: utf-8

"""
    Taxonomy API

    Use the Taxonomy API to discover the most appropriate eBay categories under which sellers can offer inventory items for sale, and the most likely categories under which buyers can browse or search for items to purchase. In addition, the Taxonomy API provides metadata about the required and recommended category aspects to include in listings, and also has two operations to retrieve parts compatibility information.  # noqa: E501

    OpenAPI spec version: v1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AspectMetadata(object):
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
        'aspects': 'list[Aspect]'
    }

    attribute_map = {
        'aspects': 'aspects'
    }

    def __init__(self, aspects=None):  # noqa: E501
        """AspectMetadata - a model defined in Swagger"""  # noqa: E501
        self._aspects = None
        self.discriminator = None
        if aspects is not None:
            self.aspects = aspects

    @property
    def aspects(self):
        """Gets the aspects of this AspectMetadata.  # noqa: E501

        A list of item aspects (for example, color) that are appropriate or necessary for accurately describing items in a particular leaf category. Each category has a different set of aspects and different requirements for aspect values. Sellers are required or encouraged to provide one or more acceptable values for each aspect when offering an item in that category on eBay.  # noqa: E501

        :return: The aspects of this AspectMetadata.  # noqa: E501
        :rtype: list[Aspect]
        """
        return self._aspects

    @aspects.setter
    def aspects(self, aspects):
        """Sets the aspects of this AspectMetadata.

        A list of item aspects (for example, color) that are appropriate or necessary for accurately describing items in a particular leaf category. Each category has a different set of aspects and different requirements for aspect values. Sellers are required or encouraged to provide one or more acceptable values for each aspect when offering an item in that category on eBay.  # noqa: E501

        :param aspects: The aspects of this AspectMetadata.  # noqa: E501
        :type: list[Aspect]
        """

        self._aspects = aspects

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
        if issubclass(AspectMetadata, dict):
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
        if not isinstance(other, AspectMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
