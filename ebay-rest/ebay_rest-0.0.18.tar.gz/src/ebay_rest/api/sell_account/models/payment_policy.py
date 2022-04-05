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

class PaymentPolicy(object):
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
        'category_types': 'list[CategoryType]',
        'deposit': 'Deposit',
        'description': 'str',
        'full_payment_due_in': 'TimeDuration',
        'immediate_pay': 'bool',
        'marketplace_id': 'str',
        'name': 'str',
        'payment_instructions': 'str',
        'payment_methods': 'list[PaymentMethod]',
        'payment_policy_id': 'str'
    }

    attribute_map = {
        'category_types': 'categoryTypes',
        'deposit': 'deposit',
        'description': 'description',
        'full_payment_due_in': 'fullPaymentDueIn',
        'immediate_pay': 'immediatePay',
        'marketplace_id': 'marketplaceId',
        'name': 'name',
        'payment_instructions': 'paymentInstructions',
        'payment_methods': 'paymentMethods',
        'payment_policy_id': 'paymentPolicyId'
    }

    def __init__(self, category_types=None, deposit=None, description=None, full_payment_due_in=None, immediate_pay=None, marketplace_id=None, name=None, payment_instructions=None, payment_methods=None, payment_policy_id=None):  # noqa: E501
        """PaymentPolicy - a model defined in Swagger"""  # noqa: E501
        self._category_types = None
        self._deposit = None
        self._description = None
        self._full_payment_due_in = None
        self._immediate_pay = None
        self._marketplace_id = None
        self._name = None
        self._payment_instructions = None
        self._payment_methods = None
        self._payment_policy_id = None
        self.discriminator = None
        if category_types is not None:
            self.category_types = category_types
        if deposit is not None:
            self.deposit = deposit
        if description is not None:
            self.description = description
        if full_payment_due_in is not None:
            self.full_payment_due_in = full_payment_due_in
        if immediate_pay is not None:
            self.immediate_pay = immediate_pay
        if marketplace_id is not None:
            self.marketplace_id = marketplace_id
        if name is not None:
            self.name = name
        if payment_instructions is not None:
            self.payment_instructions = payment_instructions
        if payment_methods is not None:
            self.payment_methods = payment_methods
        if payment_policy_id is not None:
            self.payment_policy_id = payment_policy_id

    @property
    def category_types(self):
        """Gets the category_types of this PaymentPolicy.  # noqa: E501

        This container indicates whether the fulfillment policy applies to motor vehicle listings, or if it applies to non-motor vehicle listings.  # noqa: E501

        :return: The category_types of this PaymentPolicy.  # noqa: E501
        :rtype: list[CategoryType]
        """
        return self._category_types

    @category_types.setter
    def category_types(self, category_types):
        """Sets the category_types of this PaymentPolicy.

        This container indicates whether the fulfillment policy applies to motor vehicle listings, or if it applies to non-motor vehicle listings.  # noqa: E501

        :param category_types: The category_types of this PaymentPolicy.  # noqa: E501
        :type: list[CategoryType]
        """

        self._category_types = category_types

    @property
    def deposit(self):
        """Gets the deposit of this PaymentPolicy.  # noqa: E501


        :return: The deposit of this PaymentPolicy.  # noqa: E501
        :rtype: Deposit
        """
        return self._deposit

    @deposit.setter
    def deposit(self, deposit):
        """Sets the deposit of this PaymentPolicy.


        :param deposit: The deposit of this PaymentPolicy.  # noqa: E501
        :type: Deposit
        """

        self._deposit = deposit

    @property
    def description(self):
        """Gets the description of this PaymentPolicy.  # noqa: E501

        A seller-defined description of the payment policy. This description is only for the seller's use, and is not exposed on any eBay pages.  <br/><br/><b>Max length</b>: 250  # noqa: E501

        :return: The description of this PaymentPolicy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PaymentPolicy.

        A seller-defined description of the payment policy. This description is only for the seller's use, and is not exposed on any eBay pages.  <br/><br/><b>Max length</b>: 250  # noqa: E501

        :param description: The description of this PaymentPolicy.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def full_payment_due_in(self):
        """Gets the full_payment_due_in of this PaymentPolicy.  # noqa: E501


        :return: The full_payment_due_in of this PaymentPolicy.  # noqa: E501
        :rtype: TimeDuration
        """
        return self._full_payment_due_in

    @full_payment_due_in.setter
    def full_payment_due_in(self, full_payment_due_in):
        """Sets the full_payment_due_in of this PaymentPolicy.


        :param full_payment_due_in: The full_payment_due_in of this PaymentPolicy.  # noqa: E501
        :type: TimeDuration
        """

        self._full_payment_due_in = full_payment_due_in

    @property
    def immediate_pay(self):
        """Gets the immediate_pay of this PaymentPolicy.  # noqa: E501

        If this field is returned as <code>true</code>, immediate payment is required from the buyer for: <ul><li>A fixed-price item</li><li>An auction item where the buyer uses the 'Buy it Now' option</li><li>A deposit for a motor vehicle listing</li></ul><br />It is possible for the seller to set this field as <code>true</code> in the payment business policy, but it will not apply in some scenarios. For example, immediate payment is not applicable for auction listings that have a winning bidder, for buyer purchases that involve the Best Offer feature, or for transactions that happen offline between the buyer and seller.  # noqa: E501

        :return: The immediate_pay of this PaymentPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._immediate_pay

    @immediate_pay.setter
    def immediate_pay(self, immediate_pay):
        """Sets the immediate_pay of this PaymentPolicy.

        If this field is returned as <code>true</code>, immediate payment is required from the buyer for: <ul><li>A fixed-price item</li><li>An auction item where the buyer uses the 'Buy it Now' option</li><li>A deposit for a motor vehicle listing</li></ul><br />It is possible for the seller to set this field as <code>true</code> in the payment business policy, but it will not apply in some scenarios. For example, immediate payment is not applicable for auction listings that have a winning bidder, for buyer purchases that involve the Best Offer feature, or for transactions that happen offline between the buyer and seller.  # noqa: E501

        :param immediate_pay: The immediate_pay of this PaymentPolicy.  # noqa: E501
        :type: bool
        """

        self._immediate_pay = immediate_pay

    @property
    def marketplace_id(self):
        """Gets the marketplace_id of this PaymentPolicy.  # noqa: E501

        The ID of the eBay marketplace to which the payment business policy applies. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :return: The marketplace_id of this PaymentPolicy.  # noqa: E501
        :rtype: str
        """
        return self._marketplace_id

    @marketplace_id.setter
    def marketplace_id(self, marketplace_id):
        """Sets the marketplace_id of this PaymentPolicy.

        The ID of the eBay marketplace to which the payment business policy applies. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :param marketplace_id: The marketplace_id of this PaymentPolicy.  # noqa: E501
        :type: str
        """

        self._marketplace_id = marketplace_id

    @property
    def name(self):
        """Gets the name of this PaymentPolicy.  # noqa: E501

        A seller-defined name for this fulfillment policy. Names must be unique for policies assigned to the same marketplace. <br/><br/><b>Max length</b>: 64  # noqa: E501

        :return: The name of this PaymentPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentPolicy.

        A seller-defined name for this fulfillment policy. Names must be unique for policies assigned to the same marketplace. <br/><br/><b>Max length</b>: 64  # noqa: E501

        :param name: The name of this PaymentPolicy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def payment_instructions(self):
        """Gets the payment_instructions of this PaymentPolicy.  # noqa: E501

        Although this field may be returned for some older payment business policies, payment instructions are no longer supported by payment business policies. If this field is returned, it can be ignored and these payment instructions will not appear in any listings that use the corresponding business policy. <br/><br/><b>Max length</b>: 1000  # noqa: E501

        :return: The payment_instructions of this PaymentPolicy.  # noqa: E501
        :rtype: str
        """
        return self._payment_instructions

    @payment_instructions.setter
    def payment_instructions(self, payment_instructions):
        """Sets the payment_instructions of this PaymentPolicy.

        Although this field may be returned for some older payment business policies, payment instructions are no longer supported by payment business policies. If this field is returned, it can be ignored and these payment instructions will not appear in any listings that use the corresponding business policy. <br/><br/><b>Max length</b>: 1000  # noqa: E501

        :param payment_instructions: The payment_instructions of this PaymentPolicy.  # noqa: E501
        :type: str
        """

        self._payment_instructions = payment_instructions

    @property
    def payment_methods(self):
        """Gets the payment_methods of this PaymentPolicy.  # noqa: E501

        This container is returned to show the payment methods that are accepted for the payment business policy.  <br><br>Sellers do not have to specify any electronic payment methods for listings, so this array will often be returned empty unless the payment business policy is intended for motor vehicle listings or other items in categories where offline payments are required or supported.   # noqa: E501

        :return: The payment_methods of this PaymentPolicy.  # noqa: E501
        :rtype: list[PaymentMethod]
        """
        return self._payment_methods

    @payment_methods.setter
    def payment_methods(self, payment_methods):
        """Sets the payment_methods of this PaymentPolicy.

        This container is returned to show the payment methods that are accepted for the payment business policy.  <br><br>Sellers do not have to specify any electronic payment methods for listings, so this array will often be returned empty unless the payment business policy is intended for motor vehicle listings or other items in categories where offline payments are required or supported.   # noqa: E501

        :param payment_methods: The payment_methods of this PaymentPolicy.  # noqa: E501
        :type: list[PaymentMethod]
        """

        self._payment_methods = payment_methods

    @property
    def payment_policy_id(self):
        """Gets the payment_policy_id of this PaymentPolicy.  # noqa: E501

        A unique eBay-assigned ID for a payment business policy. This ID is generated when the policy is created.  # noqa: E501

        :return: The payment_policy_id of this PaymentPolicy.  # noqa: E501
        :rtype: str
        """
        return self._payment_policy_id

    @payment_policy_id.setter
    def payment_policy_id(self, payment_policy_id):
        """Sets the payment_policy_id of this PaymentPolicy.

        A unique eBay-assigned ID for a payment business policy. This ID is generated when the policy is created.  # noqa: E501

        :param payment_policy_id: The payment_policy_id of this PaymentPolicy.  # noqa: E501
        :type: str
        """

        self._payment_policy_id = payment_policy_id

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
        if issubclass(PaymentPolicy, dict):
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
        if not isinstance(other, PaymentPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
