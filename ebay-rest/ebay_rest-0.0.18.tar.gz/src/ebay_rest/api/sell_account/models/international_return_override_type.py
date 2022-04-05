# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (eBay business policies and seller-defined custom policies), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br/><br/>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InternationalReturnOverrideType(object):
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
        'return_method': 'str',
        'return_period': 'TimeDuration',
        'returns_accepted': 'bool',
        'return_shipping_cost_payer': 'str'
    }

    attribute_map = {
        'return_method': 'returnMethod',
        'return_period': 'returnPeriod',
        'returns_accepted': 'returnsAccepted',
        'return_shipping_cost_payer': 'returnShippingCostPayer'
    }

    def __init__(self, return_method=None, return_period=None, returns_accepted=None, return_shipping_cost_payer=None):  # noqa: E501
        """InternationalReturnOverrideType - a model defined in Swagger"""  # noqa: E501
        self._return_method = None
        self._return_period = None
        self._returns_accepted = None
        self._return_shipping_cost_payer = None
        self.discriminator = None
        if return_method is not None:
            self.return_method = return_method
        if return_period is not None:
            self.return_period = return_period
        if returns_accepted is not None:
            self.returns_accepted = returns_accepted
        if return_shipping_cost_payer is not None:
            self.return_shipping_cost_payer = return_shipping_cost_payer

    @property
    def return_method(self):
        """Gets the return_method of this InternationalReturnOverrideType.  # noqa: E501

        This field sets/indicates if the seller offers replacement or exchange items to the buyer in the case of an international return. The buyer must be willing to accept a replacement or exchange item; otherwise, the seller will need to issue a refund for a return. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ReturnMethodEnum'>eBay API documentation</a>  # noqa: E501

        :return: The return_method of this InternationalReturnOverrideType.  # noqa: E501
        :rtype: str
        """
        return self._return_method

    @return_method.setter
    def return_method(self, return_method):
        """Sets the return_method of this InternationalReturnOverrideType.

        This field sets/indicates if the seller offers replacement or exchange items to the buyer in the case of an international return. The buyer must be willing to accept a replacement or exchange item; otherwise, the seller will need to issue a refund for a return. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ReturnMethodEnum'>eBay API documentation</a>  # noqa: E501

        :param return_method: The return_method of this InternationalReturnOverrideType.  # noqa: E501
        :type: str
        """

        self._return_method = return_method

    @property
    def return_period(self):
        """Gets the return_period of this InternationalReturnOverrideType.  # noqa: E501


        :return: The return_period of this InternationalReturnOverrideType.  # noqa: E501
        :rtype: TimeDuration
        """
        return self._return_period

    @return_period.setter
    def return_period(self, return_period):
        """Sets the return_period of this InternationalReturnOverrideType.


        :param return_period: The return_period of this InternationalReturnOverrideType.  # noqa: E501
        :type: TimeDuration
        """

        self._return_period = return_period

    @property
    def returns_accepted(self):
        """Gets the returns_accepted of this InternationalReturnOverrideType.  # noqa: E501

        If set to <code>true</code>, the seller accepts international returns. If set to <code>false</code>, the seller does not accept international returns.  <br/><br/>This field is conditionally required if the seller chooses to have a separate international return policy.  # noqa: E501

        :return: The returns_accepted of this InternationalReturnOverrideType.  # noqa: E501
        :rtype: bool
        """
        return self._returns_accepted

    @returns_accepted.setter
    def returns_accepted(self, returns_accepted):
        """Sets the returns_accepted of this InternationalReturnOverrideType.

        If set to <code>true</code>, the seller accepts international returns. If set to <code>false</code>, the seller does not accept international returns.  <br/><br/>This field is conditionally required if the seller chooses to have a separate international return policy.  # noqa: E501

        :param returns_accepted: The returns_accepted of this InternationalReturnOverrideType.  # noqa: E501
        :type: bool
        """

        self._returns_accepted = returns_accepted

    @property
    def return_shipping_cost_payer(self):
        """Gets the return_shipping_cost_payer of this InternationalReturnOverrideType.  # noqa: E501

        This field indicates who is responsible for paying for the shipping charges for returned items. The field can be set to either <code>BUYER</code> or <code>SELLER</code>.  <br/><br/>Depending on the return policy and specifics of the return, either the buyer or the seller can be responsible for the return shipping costs. Note that the seller is always responsible for return shipping costs for 'significantly not as described' (SNAD) issues.  <br/><br/>This field is conditionally required if the <b>internationalOverride.returnsAccepted</b> field is set to <code>true</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ReturnShippingCostPayerEnum'>eBay API documentation</a>  # noqa: E501

        :return: The return_shipping_cost_payer of this InternationalReturnOverrideType.  # noqa: E501
        :rtype: str
        """
        return self._return_shipping_cost_payer

    @return_shipping_cost_payer.setter
    def return_shipping_cost_payer(self, return_shipping_cost_payer):
        """Sets the return_shipping_cost_payer of this InternationalReturnOverrideType.

        This field indicates who is responsible for paying for the shipping charges for returned items. The field can be set to either <code>BUYER</code> or <code>SELLER</code>.  <br/><br/>Depending on the return policy and specifics of the return, either the buyer or the seller can be responsible for the return shipping costs. Note that the seller is always responsible for return shipping costs for 'significantly not as described' (SNAD) issues.  <br/><br/>This field is conditionally required if the <b>internationalOverride.returnsAccepted</b> field is set to <code>true</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ReturnShippingCostPayerEnum'>eBay API documentation</a>  # noqa: E501

        :param return_shipping_cost_payer: The return_shipping_cost_payer of this InternationalReturnOverrideType.  # noqa: E501
        :type: str
        """

        self._return_shipping_cost_payer = return_shipping_cost_payer

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
        if issubclass(InternationalReturnOverrideType, dict):
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
        if not isinstance(other, InternationalReturnOverrideType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
