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

class Tax(object):
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
        'apply_tax': 'bool',
        'third_party_tax_category': 'str',
        'vat_percentage': 'float'
    }

    attribute_map = {
        'apply_tax': 'applyTax',
        'third_party_tax_category': 'thirdPartyTaxCategory',
        'vat_percentage': 'vatPercentage'
    }

    def __init__(self, apply_tax=None, third_party_tax_category=None, vat_percentage=None):  # noqa: E501
        """Tax - a model defined in Swagger"""  # noqa: E501
        self._apply_tax = None
        self._third_party_tax_category = None
        self._vat_percentage = None
        self.discriminator = None
        if apply_tax is not None:
            self.apply_tax = apply_tax
        if third_party_tax_category is not None:
            self.third_party_tax_category = third_party_tax_category
        if vat_percentage is not None:
            self.vat_percentage = vat_percentage

    @property
    def apply_tax(self):
        """Gets the apply_tax of this Tax.  # noqa: E501

        This field will be included and set to <code>true</code> if the seller would like to reference their account-level Sales Tax Table to calculate sales tax for an order. A seller's Sales Tax Table can be created and managed manually in My eBay's Payment Preferences. This Sales Tax Table contains all tax jurisdictions for the seller's country (individual states and territories in US), and the seller can set the sales tax rate for these individual tax jurisdictions. <br/><br/> The Trading API has a <a href=\"https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/SetTaxTable.html\" target=\"_blank\">SetTaxTable</a> call to add/modify sales tax rates for one or more tax jurisdictions, and a <a href=\"https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetTaxTable.html\" target=\"_blank\">GetTaxTable</a> call that will retrieve all tax jurisdictions and related data, such as the sales tax rate (if defined) and a boolean field to indicate if sales tax is applied to shipping and handling costs.<br/><br/> The Account API has a <strong>getSalesTaxTable</strong> call to retrieve all tax jurisdictions that have a defined sales tax rate, a <strong>getSalesTaxTableEntry</strong> call to retrieve a sales tax rate for a specific tax jurisdiction, a <strong>createSalesTaxTableEntry</strong> call to set/modify a sales tax rate for a specific tax jurisdiction, and a <strong>deleteSalesTaxTableEntry</strong> call to remove a sales tax rate from a specific tax jurisdiction. <br/><br/>Note that a seller can enable the use of a sales tax table, but if a sales tax rate is not specified for the buyer's state/tax jurisdiction, sales tax will not be applied to the order. If a <strong>thirdPartyTaxCategory</strong> value is used, the <strong>applyTax</strong> field must also be used and set to <code>true</code><br/><br/>This field will be returned if set for the offer.<br/><br/>See the <a href=\"https://pages.ebay.com/help/pay/checkout-tax-table.html\" target=\"_blank\">Using a tax table</a> help page for more information on setting up and using a sales tax table.  # noqa: E501

        :return: The apply_tax of this Tax.  # noqa: E501
        :rtype: bool
        """
        return self._apply_tax

    @apply_tax.setter
    def apply_tax(self, apply_tax):
        """Sets the apply_tax of this Tax.

        This field will be included and set to <code>true</code> if the seller would like to reference their account-level Sales Tax Table to calculate sales tax for an order. A seller's Sales Tax Table can be created and managed manually in My eBay's Payment Preferences. This Sales Tax Table contains all tax jurisdictions for the seller's country (individual states and territories in US), and the seller can set the sales tax rate for these individual tax jurisdictions. <br/><br/> The Trading API has a <a href=\"https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/SetTaxTable.html\" target=\"_blank\">SetTaxTable</a> call to add/modify sales tax rates for one or more tax jurisdictions, and a <a href=\"https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/GetTaxTable.html\" target=\"_blank\">GetTaxTable</a> call that will retrieve all tax jurisdictions and related data, such as the sales tax rate (if defined) and a boolean field to indicate if sales tax is applied to shipping and handling costs.<br/><br/> The Account API has a <strong>getSalesTaxTable</strong> call to retrieve all tax jurisdictions that have a defined sales tax rate, a <strong>getSalesTaxTableEntry</strong> call to retrieve a sales tax rate for a specific tax jurisdiction, a <strong>createSalesTaxTableEntry</strong> call to set/modify a sales tax rate for a specific tax jurisdiction, and a <strong>deleteSalesTaxTableEntry</strong> call to remove a sales tax rate from a specific tax jurisdiction. <br/><br/>Note that a seller can enable the use of a sales tax table, but if a sales tax rate is not specified for the buyer's state/tax jurisdiction, sales tax will not be applied to the order. If a <strong>thirdPartyTaxCategory</strong> value is used, the <strong>applyTax</strong> field must also be used and set to <code>true</code><br/><br/>This field will be returned if set for the offer.<br/><br/>See the <a href=\"https://pages.ebay.com/help/pay/checkout-tax-table.html\" target=\"_blank\">Using a tax table</a> help page for more information on setting up and using a sales tax table.  # noqa: E501

        :param apply_tax: The apply_tax of this Tax.  # noqa: E501
        :type: bool
        """

        self._apply_tax = apply_tax

    @property
    def third_party_tax_category(self):
        """Gets the third_party_tax_category of this Tax.  # noqa: E501

        The tax exception category code. If this field is used, sales tax will also apply to a service/fee, and not just the item price. This is to be used only by sellers who have opted into sales tax being calculated by a sales tax calculation vendor. If you are interested in becoming a tax calculation vendor partner with eBay, contact <a href=\"mailto:developer-relations@ebay.com\">developer-relations@ebay.com</a>. One supported value for this field is <code>WASTE_RECYCLING_FEE</code>. If this field is used, the <strong>applyTax</strong> field must also be used and set to <code>true</code><br/><br/>This field will be returned if set for the offer.  # noqa: E501

        :return: The third_party_tax_category of this Tax.  # noqa: E501
        :rtype: str
        """
        return self._third_party_tax_category

    @third_party_tax_category.setter
    def third_party_tax_category(self, third_party_tax_category):
        """Sets the third_party_tax_category of this Tax.

        The tax exception category code. If this field is used, sales tax will also apply to a service/fee, and not just the item price. This is to be used only by sellers who have opted into sales tax being calculated by a sales tax calculation vendor. If you are interested in becoming a tax calculation vendor partner with eBay, contact <a href=\"mailto:developer-relations@ebay.com\">developer-relations@ebay.com</a>. One supported value for this field is <code>WASTE_RECYCLING_FEE</code>. If this field is used, the <strong>applyTax</strong> field must also be used and set to <code>true</code><br/><br/>This field will be returned if set for the offer.  # noqa: E501

        :param third_party_tax_category: The third_party_tax_category of this Tax.  # noqa: E501
        :type: str
        """

        self._third_party_tax_category = third_party_tax_category

    @property
    def vat_percentage(self):
        """Gets the vat_percentage of this Tax.  # noqa: E501

        This value is the Value Add Tax (VAT) rate for the item, if any. When a VAT percentage is specified, the item's VAT information appears on the listing's View Item page. In addition, the seller can choose to print an invoice that includes the item's net price, VAT percent, VAT amount, and total price. Since VAT rates vary depending on the item and on the user's country of residence, a seller is responsible for entering the correct VAT rate; it is not calculated by eBay. <br/><br/> To use VAT, a seller must be a business seller with a VAT-ID registered with eBay, and must be listing the item on a VAT-enabled site. Max applicable length is 6 characters, including the decimal (e.g., 12.345). The scale is 3 decimal places. (If you pass in 12.3456, eBay may round up the value to 12.346).<br/><br/>This field will be returned if set for the offer.  # noqa: E501

        :return: The vat_percentage of this Tax.  # noqa: E501
        :rtype: float
        """
        return self._vat_percentage

    @vat_percentage.setter
    def vat_percentage(self, vat_percentage):
        """Sets the vat_percentage of this Tax.

        This value is the Value Add Tax (VAT) rate for the item, if any. When a VAT percentage is specified, the item's VAT information appears on the listing's View Item page. In addition, the seller can choose to print an invoice that includes the item's net price, VAT percent, VAT amount, and total price. Since VAT rates vary depending on the item and on the user's country of residence, a seller is responsible for entering the correct VAT rate; it is not calculated by eBay. <br/><br/> To use VAT, a seller must be a business seller with a VAT-ID registered with eBay, and must be listing the item on a VAT-enabled site. Max applicable length is 6 characters, including the decimal (e.g., 12.345). The scale is 3 decimal places. (If you pass in 12.3456, eBay may round up the value to 12.346).<br/><br/>This field will be returned if set for the offer.  # noqa: E501

        :param vat_percentage: The vat_percentage of this Tax.  # noqa: E501
        :type: float
        """

        self._vat_percentage = vat_percentage

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
        if issubclass(Tax, dict):
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
        if not isinstance(other, Tax):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
