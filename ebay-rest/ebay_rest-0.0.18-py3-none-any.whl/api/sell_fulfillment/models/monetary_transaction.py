# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MonetaryTransaction(object):
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
        'amount': 'DisputeAmount',
        '_date': 'str',
        'reason': 'str',
        'type': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        '_date': 'date',
        'reason': 'reason',
        'type': 'type'
    }

    def __init__(self, amount=None, _date=None, reason=None, type=None):  # noqa: E501
        """MonetaryTransaction - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self.__date = None
        self._reason = None
        self._type = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if _date is not None:
            self._date = _date
        if reason is not None:
            self.reason = reason
        if type is not None:
            self.type = type

    @property
    def amount(self):
        """Gets the amount of this MonetaryTransaction.  # noqa: E501


        :return: The amount of this MonetaryTransaction.  # noqa: E501
        :rtype: DisputeAmount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this MonetaryTransaction.


        :param amount: The amount of this MonetaryTransaction.  # noqa: E501
        :type: DisputeAmount
        """

        self._amount = amount

    @property
    def _date(self):
        """Gets the _date of this MonetaryTransaction.  # noqa: E501

        This timestamp indicates when the monetary transaction occurred. A date is returned for all monetary transactions.<br><br> The following format is used: <code>YYYY-MM-DDTHH:MM:SS.SSSZ</code>. For example, <code>2015-08-04T19:09:02.768Z</code>.  # noqa: E501

        :return: The _date of this MonetaryTransaction.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this MonetaryTransaction.

        This timestamp indicates when the monetary transaction occurred. A date is returned for all monetary transactions.<br><br> The following format is used: <code>YYYY-MM-DDTHH:MM:SS.SSSZ</code>. For example, <code>2015-08-04T19:09:02.768Z</code>.  # noqa: E501

        :param _date: The _date of this MonetaryTransaction.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def reason(self):
        """Gets the reason of this MonetaryTransaction.  # noqa: E501

        This enumeration value indicates the reason for the monetary transaction. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:MonetaryTransactionReasonEnum'>eBay API documentation</a>  # noqa: E501

        :return: The reason of this MonetaryTransaction.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this MonetaryTransaction.

        This enumeration value indicates the reason for the monetary transaction. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:MonetaryTransactionReasonEnum'>eBay API documentation</a>  # noqa: E501

        :param reason: The reason of this MonetaryTransaction.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def type(self):
        """Gets the type of this MonetaryTransaction.  # noqa: E501

        This enumeration value indicates whether the monetary transaction is a charge or a credit to the seller. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:MonetaryTransactionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The type of this MonetaryTransaction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MonetaryTransaction.

        This enumeration value indicates whether the monetary transaction is a charge or a credit to the seller. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:MonetaryTransactionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param type: The type of this MonetaryTransaction.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(MonetaryTransaction, dict):
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
        if not isinstance(other, MonetaryTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
