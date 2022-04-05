# coding: utf-8

"""
    Catalog API

    The Catalog API allows users to search for and locate an eBay catalog product that is a direct match for the product that they wish to sell. Listing against an eBay catalog product helps insure that all listings (based off of that catalog product) have complete and accurate information. In addition to helping to create high-quality listings, another benefit to the seller of using catalog information to create listings is that much of the details of the listing will be prefilled, including the listing title, the listing description, the item specifics, and a stock image for the product (if available). Sellers will not have to enter item specifics themselves, and the overall listing process is a lot faster and easier.  # noqa: E501

    OpenAPI spec version: v1_beta.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AspectDistribution(object):
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
        'aspect_value_distributions': 'list[AspectValueDistribution]',
        'localized_aspect_name': 'str'
    }

    attribute_map = {
        'aspect_value_distributions': 'aspectValueDistributions',
        'localized_aspect_name': 'localizedAspectName'
    }

    def __init__(self, aspect_value_distributions=None, localized_aspect_name=None):  # noqa: E501
        """AspectDistribution - a model defined in Swagger"""  # noqa: E501
        self._aspect_value_distributions = None
        self._localized_aspect_name = None
        self.discriminator = None
        if aspect_value_distributions is not None:
            self.aspect_value_distributions = aspect_value_distributions
        if localized_aspect_name is not None:
            self.localized_aspect_name = localized_aspect_name

    @property
    def aspect_value_distributions(self):
        """Gets the aspect_value_distributions of this AspectDistribution.  # noqa: E501

        Contains information about one or more values of the category aspect identified by localizedAspectName.  # noqa: E501

        :return: The aspect_value_distributions of this AspectDistribution.  # noqa: E501
        :rtype: list[AspectValueDistribution]
        """
        return self._aspect_value_distributions

    @aspect_value_distributions.setter
    def aspect_value_distributions(self, aspect_value_distributions):
        """Sets the aspect_value_distributions of this AspectDistribution.

        Contains information about one or more values of the category aspect identified by localizedAspectName.  # noqa: E501

        :param aspect_value_distributions: The aspect_value_distributions of this AspectDistribution.  # noqa: E501
        :type: list[AspectValueDistribution]
        """

        self._aspect_value_distributions = aspect_value_distributions

    @property
    def localized_aspect_name(self):
        """Gets the localized_aspect_name of this AspectDistribution.  # noqa: E501

        The localized name of an aspect that is associated with the category identified by dominantCategoryId.  # noqa: E501

        :return: The localized_aspect_name of this AspectDistribution.  # noqa: E501
        :rtype: str
        """
        return self._localized_aspect_name

    @localized_aspect_name.setter
    def localized_aspect_name(self, localized_aspect_name):
        """Sets the localized_aspect_name of this AspectDistribution.

        The localized name of an aspect that is associated with the category identified by dominantCategoryId.  # noqa: E501

        :param localized_aspect_name: The localized_aspect_name of this AspectDistribution.  # noqa: E501
        :type: str
        """

        self._localized_aspect_name = localized_aspect_name

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
        if issubclass(AspectDistribution, dict):
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
        if not isinstance(other, AspectDistribution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
