# coding: utf-8

"""
    Browse API

    <p>The Browse API has the following resources:</p>   <ul> <li><b> item_summary: </b> Lets shoppers search for specific items by keyword, GTIN, category, charity, product, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values.</li>  <li><b> search_by_image: </b><a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> Lets shoppers search for specific items by image. You can refine the results by using URI parameters and filters.</li>   <li><b> item: </b> <ul><li>Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.</li> <li>Provides a bridge between the eBay legacy APIs, such as <b> Finding</b>, and the RESTful APIs, which use different formats for the item IDs.</li>  </ul> </li>  <li> <b> shopping_cart: </b> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited \" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> Provides the ability for eBay members to see the contents of their eBay cart, and add, remove, and change the quantity of items in their eBay cart.&nbsp;&nbsp;<b> Note: </b> This resource is not available in the eBay API Explorer.</li></ul>       <p>The <b> item_summary</b>, <b> search_by_image</b>, and <b> item</b> resource calls require an <a href=\"/api-docs/static/oauth-client-credentials-grant.html\">Application access token</a>. The <b> shopping_cart</b> resource calls require a <a href=\"/api-docs/static/oauth-authorization-code-grant.html\">User access token</a>.</p>  # noqa: E501

    OpenAPI spec version: v1.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SellerLegalInfo(object):
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
        'email': 'str',
        'fax': 'str',
        'imprint': 'str',
        'legal_contact_first_name': 'str',
        'legal_contact_last_name': 'str',
        'name': 'str',
        'phone': 'str',
        'registration_number': 'str',
        'seller_provided_legal_address': 'LegalAddress',
        'terms_of_service': 'str',
        'vat_details': 'list[VatDetail]'
    }

    attribute_map = {
        'email': 'email',
        'fax': 'fax',
        'imprint': 'imprint',
        'legal_contact_first_name': 'legalContactFirstName',
        'legal_contact_last_name': 'legalContactLastName',
        'name': 'name',
        'phone': 'phone',
        'registration_number': 'registrationNumber',
        'seller_provided_legal_address': 'sellerProvidedLegalAddress',
        'terms_of_service': 'termsOfService',
        'vat_details': 'vatDetails'
    }

    def __init__(self, email=None, fax=None, imprint=None, legal_contact_first_name=None, legal_contact_last_name=None, name=None, phone=None, registration_number=None, seller_provided_legal_address=None, terms_of_service=None, vat_details=None):  # noqa: E501
        """SellerLegalInfo - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._fax = None
        self._imprint = None
        self._legal_contact_first_name = None
        self._legal_contact_last_name = None
        self._name = None
        self._phone = None
        self._registration_number = None
        self._seller_provided_legal_address = None
        self._terms_of_service = None
        self._vat_details = None
        self.discriminator = None
        if email is not None:
            self.email = email
        if fax is not None:
            self.fax = fax
        if imprint is not None:
            self.imprint = imprint
        if legal_contact_first_name is not None:
            self.legal_contact_first_name = legal_contact_first_name
        if legal_contact_last_name is not None:
            self.legal_contact_last_name = legal_contact_last_name
        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone
        if registration_number is not None:
            self.registration_number = registration_number
        if seller_provided_legal_address is not None:
            self.seller_provided_legal_address = seller_provided_legal_address
        if terms_of_service is not None:
            self.terms_of_service = terms_of_service
        if vat_details is not None:
            self.vat_details = vat_details

    @property
    def email(self):
        """Gets the email of this SellerLegalInfo.  # noqa: E501

        The seller's business email address.  # noqa: E501

        :return: The email of this SellerLegalInfo.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SellerLegalInfo.

        The seller's business email address.  # noqa: E501

        :param email: The email of this SellerLegalInfo.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def fax(self):
        """Gets the fax of this SellerLegalInfo.  # noqa: E501

        The seller' business fax number.  # noqa: E501

        :return: The fax of this SellerLegalInfo.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this SellerLegalInfo.

        The seller' business fax number.  # noqa: E501

        :param fax: The fax of this SellerLegalInfo.  # noqa: E501
        :type: str
        """

        self._fax = fax

    @property
    def imprint(self):
        """Gets the imprint of this SellerLegalInfo.  # noqa: E501

        This is a free-form string created by the seller. This is information often found on business cards, such as address. This is information used by some countries.  # noqa: E501

        :return: The imprint of this SellerLegalInfo.  # noqa: E501
        :rtype: str
        """
        return self._imprint

    @imprint.setter
    def imprint(self, imprint):
        """Sets the imprint of this SellerLegalInfo.

        This is a free-form string created by the seller. This is information often found on business cards, such as address. This is information used by some countries.  # noqa: E501

        :param imprint: The imprint of this SellerLegalInfo.  # noqa: E501
        :type: str
        """

        self._imprint = imprint

    @property
    def legal_contact_first_name(self):
        """Gets the legal_contact_first_name of this SellerLegalInfo.  # noqa: E501

        The seller's first name.  # noqa: E501

        :return: The legal_contact_first_name of this SellerLegalInfo.  # noqa: E501
        :rtype: str
        """
        return self._legal_contact_first_name

    @legal_contact_first_name.setter
    def legal_contact_first_name(self, legal_contact_first_name):
        """Sets the legal_contact_first_name of this SellerLegalInfo.

        The seller's first name.  # noqa: E501

        :param legal_contact_first_name: The legal_contact_first_name of this SellerLegalInfo.  # noqa: E501
        :type: str
        """

        self._legal_contact_first_name = legal_contact_first_name

    @property
    def legal_contact_last_name(self):
        """Gets the legal_contact_last_name of this SellerLegalInfo.  # noqa: E501

        The seller's last name.  # noqa: E501

        :return: The legal_contact_last_name of this SellerLegalInfo.  # noqa: E501
        :rtype: str
        """
        return self._legal_contact_last_name

    @legal_contact_last_name.setter
    def legal_contact_last_name(self, legal_contact_last_name):
        """Sets the legal_contact_last_name of this SellerLegalInfo.

        The seller's last name.  # noqa: E501

        :param legal_contact_last_name: The legal_contact_last_name of this SellerLegalInfo.  # noqa: E501
        :type: str
        """

        self._legal_contact_last_name = legal_contact_last_name

    @property
    def name(self):
        """Gets the name of this SellerLegalInfo.  # noqa: E501

        The name of the seller's business.  # noqa: E501

        :return: The name of this SellerLegalInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SellerLegalInfo.

        The name of the seller's business.  # noqa: E501

        :param name: The name of this SellerLegalInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phone(self):
        """Gets the phone of this SellerLegalInfo.  # noqa: E501

        The seller's business phone number.  # noqa: E501

        :return: The phone of this SellerLegalInfo.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this SellerLegalInfo.

        The seller's business phone number.  # noqa: E501

        :param phone: The phone of this SellerLegalInfo.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def registration_number(self):
        """Gets the registration_number of this SellerLegalInfo.  # noqa: E501

        The seller's registration number. This is information used by some countries.  # noqa: E501

        :return: The registration_number of this SellerLegalInfo.  # noqa: E501
        :rtype: str
        """
        return self._registration_number

    @registration_number.setter
    def registration_number(self, registration_number):
        """Sets the registration_number of this SellerLegalInfo.

        The seller's registration number. This is information used by some countries.  # noqa: E501

        :param registration_number: The registration_number of this SellerLegalInfo.  # noqa: E501
        :type: str
        """

        self._registration_number = registration_number

    @property
    def seller_provided_legal_address(self):
        """Gets the seller_provided_legal_address of this SellerLegalInfo.  # noqa: E501


        :return: The seller_provided_legal_address of this SellerLegalInfo.  # noqa: E501
        :rtype: LegalAddress
        """
        return self._seller_provided_legal_address

    @seller_provided_legal_address.setter
    def seller_provided_legal_address(self, seller_provided_legal_address):
        """Sets the seller_provided_legal_address of this SellerLegalInfo.


        :param seller_provided_legal_address: The seller_provided_legal_address of this SellerLegalInfo.  # noqa: E501
        :type: LegalAddress
        """

        self._seller_provided_legal_address = seller_provided_legal_address

    @property
    def terms_of_service(self):
        """Gets the terms_of_service of this SellerLegalInfo.  # noqa: E501

        This is a free-form string created by the seller. This is the seller's terms or condition, which is in addition to the seller's return policies.  # noqa: E501

        :return: The terms_of_service of this SellerLegalInfo.  # noqa: E501
        :rtype: str
        """
        return self._terms_of_service

    @terms_of_service.setter
    def terms_of_service(self, terms_of_service):
        """Sets the terms_of_service of this SellerLegalInfo.

        This is a free-form string created by the seller. This is the seller's terms or condition, which is in addition to the seller's return policies.  # noqa: E501

        :param terms_of_service: The terms_of_service of this SellerLegalInfo.  # noqa: E501
        :type: str
        """

        self._terms_of_service = terms_of_service

    @property
    def vat_details(self):
        """Gets the vat_details of this SellerLegalInfo.  # noqa: E501

        An array of the seller's VAT (value added tax) IDs and the issuing country. VAT is a tax added by some European countries.  # noqa: E501

        :return: The vat_details of this SellerLegalInfo.  # noqa: E501
        :rtype: list[VatDetail]
        """
        return self._vat_details

    @vat_details.setter
    def vat_details(self, vat_details):
        """Sets the vat_details of this SellerLegalInfo.

        An array of the seller's VAT (value added tax) IDs and the issuing country. VAT is a tax added by some European countries.  # noqa: E501

        :param vat_details: The vat_details of this SellerLegalInfo.  # noqa: E501
        :type: list[VatDetail]
        """

        self._vat_details = vat_details

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
        if issubclass(SellerLegalInfo, dict):
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
        if not isinstance(other, SellerLegalInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
