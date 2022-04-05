# coding: utf-8

"""
    Metadata API

    The Metadata API has operations that retrieve configuration details pertaining to the different eBay marketplaces. In addition to marketplace information, the API also has operations that get information that helps sellers list items on eBay.  # noqa: E501

    OpenAPI spec version: v1.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NegotiatedPricePolicyResponse(object):
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
        'negotiated_price_policies': 'list[NegotiatedPricePolicy]',
        'warnings': 'list[Error]'
    }

    attribute_map = {
        'negotiated_price_policies': 'negotiatedPricePolicies',
        'warnings': 'warnings'
    }

    def __init__(self, negotiated_price_policies=None, warnings=None):  # noqa: E501
        """NegotiatedPricePolicyResponse - a model defined in Swagger"""  # noqa: E501
        self._negotiated_price_policies = None
        self._warnings = None
        self.discriminator = None
        if negotiated_price_policies is not None:
            self.negotiated_price_policies = negotiated_price_policies
        if warnings is not None:
            self.warnings = warnings

    @property
    def negotiated_price_policies(self):
        """Gets the negotiated_price_policies of this NegotiatedPricePolicyResponse.  # noqa: E501

        A list of category IDs and the policies related to negotiated-price items for each of the listed categories.  # noqa: E501

        :return: The negotiated_price_policies of this NegotiatedPricePolicyResponse.  # noqa: E501
        :rtype: list[NegotiatedPricePolicy]
        """
        return self._negotiated_price_policies

    @negotiated_price_policies.setter
    def negotiated_price_policies(self, negotiated_price_policies):
        """Sets the negotiated_price_policies of this NegotiatedPricePolicyResponse.

        A list of category IDs and the policies related to negotiated-price items for each of the listed categories.  # noqa: E501

        :param negotiated_price_policies: The negotiated_price_policies of this NegotiatedPricePolicyResponse.  # noqa: E501
        :type: list[NegotiatedPricePolicy]
        """

        self._negotiated_price_policies = negotiated_price_policies

    @property
    def warnings(self):
        """Gets the warnings of this NegotiatedPricePolicyResponse.  # noqa: E501

        A list of the warnings that were generated as a result of the request. This field is not returned if no warnings were generated by the request.  # noqa: E501

        :return: The warnings of this NegotiatedPricePolicyResponse.  # noqa: E501
        :rtype: list[Error]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this NegotiatedPricePolicyResponse.

        A list of the warnings that were generated as a result of the request. This field is not returned if no warnings were generated by the request.  # noqa: E501

        :param warnings: The warnings of this NegotiatedPricePolicyResponse.  # noqa: E501
        :type: list[Error]
        """

        self._warnings = warnings

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
        if issubclass(NegotiatedPricePolicyResponse, dict):
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
        if not isinstance(other, NegotiatedPricePolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
