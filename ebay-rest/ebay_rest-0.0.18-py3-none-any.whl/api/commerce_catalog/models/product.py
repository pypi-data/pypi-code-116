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

class Product(object):
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
        'additional_images': 'list[Image]',
        'aspects': 'list[Aspect]',
        'brand': 'str',
        'description': 'str',
        'ean': 'list[str]',
        'epid': 'str',
        'gtin': 'list[str]',
        'image': 'Image',
        'isbn': 'list[str]',
        'mpn': 'list[str]',
        'other_applicable_category_ids': 'list[str]',
        'primary_category_id': 'str',
        'product_web_url': 'str',
        'title': 'str',
        'upc': 'list[str]',
        'version': 'str'
    }

    attribute_map = {
        'additional_images': 'additionalImages',
        'aspects': 'aspects',
        'brand': 'brand',
        'description': 'description',
        'ean': 'ean',
        'epid': 'epid',
        'gtin': 'gtin',
        'image': 'image',
        'isbn': 'isbn',
        'mpn': 'mpn',
        'other_applicable_category_ids': 'otherApplicableCategoryIds',
        'primary_category_id': 'primaryCategoryId',
        'product_web_url': 'productWebUrl',
        'title': 'title',
        'upc': 'upc',
        'version': 'version'
    }

    def __init__(self, additional_images=None, aspects=None, brand=None, description=None, ean=None, epid=None, gtin=None, image=None, isbn=None, mpn=None, other_applicable_category_ids=None, primary_category_id=None, product_web_url=None, title=None, upc=None, version=None):  # noqa: E501
        """Product - a model defined in Swagger"""  # noqa: E501
        self._additional_images = None
        self._aspects = None
        self._brand = None
        self._description = None
        self._ean = None
        self._epid = None
        self._gtin = None
        self._image = None
        self._isbn = None
        self._mpn = None
        self._other_applicable_category_ids = None
        self._primary_category_id = None
        self._product_web_url = None
        self._title = None
        self._upc = None
        self._version = None
        self.discriminator = None
        if additional_images is not None:
            self.additional_images = additional_images
        if aspects is not None:
            self.aspects = aspects
        if brand is not None:
            self.brand = brand
        if description is not None:
            self.description = description
        if ean is not None:
            self.ean = ean
        if epid is not None:
            self.epid = epid
        if gtin is not None:
            self.gtin = gtin
        if image is not None:
            self.image = image
        if isbn is not None:
            self.isbn = isbn
        if mpn is not None:
            self.mpn = mpn
        if other_applicable_category_ids is not None:
            self.other_applicable_category_ids = other_applicable_category_ids
        if primary_category_id is not None:
            self.primary_category_id = primary_category_id
        if product_web_url is not None:
            self.product_web_url = product_web_url
        if title is not None:
            self.title = title
        if upc is not None:
            self.upc = upc
        if version is not None:
            self.version = version

    @property
    def additional_images(self):
        """Gets the additional_images of this Product.  # noqa: E501

        Contains information about additional images associated with this product. For the primary image, see the image container.  # noqa: E501

        :return: The additional_images of this Product.  # noqa: E501
        :rtype: list[Image]
        """
        return self._additional_images

    @additional_images.setter
    def additional_images(self, additional_images):
        """Sets the additional_images of this Product.

        Contains information about additional images associated with this product. For the primary image, see the image container.  # noqa: E501

        :param additional_images: The additional_images of this Product.  # noqa: E501
        :type: list[Image]
        """

        self._additional_images = additional_images

    @property
    def aspects(self):
        """Gets the aspects of this Product.  # noqa: E501

        Contains an array of the category aspects and their values that are associated with this product.  # noqa: E501

        :return: The aspects of this Product.  # noqa: E501
        :rtype: list[Aspect]
        """
        return self._aspects

    @aspects.setter
    def aspects(self, aspects):
        """Sets the aspects of this Product.

        Contains an array of the category aspects and their values that are associated with this product.  # noqa: E501

        :param aspects: The aspects of this Product.  # noqa: E501
        :type: list[Aspect]
        """

        self._aspects = aspects

    @property
    def brand(self):
        """Gets the brand of this Product.  # noqa: E501

        The manufacturer's brand name for this product.  # noqa: E501

        :return: The brand of this Product.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this Product.

        The manufacturer's brand name for this product.  # noqa: E501

        :param brand: The brand of this Product.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def description(self):
        """Gets the description of this Product.  # noqa: E501

        The rich description of this product, which might contain HTML.  # noqa: E501

        :return: The description of this Product.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Product.

        The rich description of this product, which might contain HTML.  # noqa: E501

        :param description: The description of this Product.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ean(self):
        """Gets the ean of this Product.  # noqa: E501

        A list of all European Article Numbers (EANs) that identify this product.  # noqa: E501

        :return: The ean of this Product.  # noqa: E501
        :rtype: list[str]
        """
        return self._ean

    @ean.setter
    def ean(self, ean):
        """Sets the ean of this Product.

        A list of all European Article Numbers (EANs) that identify this product.  # noqa: E501

        :param ean: The ean of this Product.  # noqa: E501
        :type: list[str]
        """

        self._ean = ean

    @property
    def epid(self):
        """Gets the epid of this Product.  # noqa: E501

        The eBay product ID of this product.  # noqa: E501

        :return: The epid of this Product.  # noqa: E501
        :rtype: str
        """
        return self._epid

    @epid.setter
    def epid(self, epid):
        """Sets the epid of this Product.

        The eBay product ID of this product.  # noqa: E501

        :param epid: The epid of this Product.  # noqa: E501
        :type: str
        """

        self._epid = epid

    @property
    def gtin(self):
        """Gets the gtin of this Product.  # noqa: E501

        A list of all GTINs that identify this product. Currently this can include EAN, ISBN, and UPC identifier types.  # noqa: E501

        :return: The gtin of this Product.  # noqa: E501
        :rtype: list[str]
        """
        return self._gtin

    @gtin.setter
    def gtin(self, gtin):
        """Sets the gtin of this Product.

        A list of all GTINs that identify this product. Currently this can include EAN, ISBN, and UPC identifier types.  # noqa: E501

        :param gtin: The gtin of this Product.  # noqa: E501
        :type: list[str]
        """

        self._gtin = gtin

    @property
    def image(self):
        """Gets the image of this Product.  # noqa: E501


        :return: The image of this Product.  # noqa: E501
        :rtype: Image
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Product.


        :param image: The image of this Product.  # noqa: E501
        :type: Image
        """

        self._image = image

    @property
    def isbn(self):
        """Gets the isbn of this Product.  # noqa: E501

        A list of all International Standard Book Numbers (ISBNs) that identify this product.  # noqa: E501

        :return: The isbn of this Product.  # noqa: E501
        :rtype: list[str]
        """
        return self._isbn

    @isbn.setter
    def isbn(self, isbn):
        """Sets the isbn of this Product.

        A list of all International Standard Book Numbers (ISBNs) that identify this product.  # noqa: E501

        :param isbn: The isbn of this Product.  # noqa: E501
        :type: list[str]
        """

        self._isbn = isbn

    @property
    def mpn(self):
        """Gets the mpn of this Product.  # noqa: E501

        A list of all MPN values that the manufacturer uses to identify this product.  # noqa: E501

        :return: The mpn of this Product.  # noqa: E501
        :rtype: list[str]
        """
        return self._mpn

    @mpn.setter
    def mpn(self, mpn):
        """Sets the mpn of this Product.

        A list of all MPN values that the manufacturer uses to identify this product.  # noqa: E501

        :param mpn: The mpn of this Product.  # noqa: E501
        :type: list[str]
        """

        self._mpn = mpn

    @property
    def other_applicable_category_ids(self):
        """Gets the other_applicable_category_ids of this Product.  # noqa: E501

        A list of category IDs (other than the value of primaryCategoryId) for all the leaf categories to which this product might belong.  # noqa: E501

        :return: The other_applicable_category_ids of this Product.  # noqa: E501
        :rtype: list[str]
        """
        return self._other_applicable_category_ids

    @other_applicable_category_ids.setter
    def other_applicable_category_ids(self, other_applicable_category_ids):
        """Sets the other_applicable_category_ids of this Product.

        A list of category IDs (other than the value of primaryCategoryId) for all the leaf categories to which this product might belong.  # noqa: E501

        :param other_applicable_category_ids: The other_applicable_category_ids of this Product.  # noqa: E501
        :type: list[str]
        """

        self._other_applicable_category_ids = other_applicable_category_ids

    @property
    def primary_category_id(self):
        """Gets the primary_category_id of this Product.  # noqa: E501

        The identifier of the leaf category that eBay recommends using to list this product, based on previous listings of similar products. Products in the eBay catalog are not automatically associated with any particular category, but using an inappropriate category can make it difficult for prospective buyers to find the product. For other possible categories that might be used, see otherApplicableCategoryIds.  # noqa: E501

        :return: The primary_category_id of this Product.  # noqa: E501
        :rtype: str
        """
        return self._primary_category_id

    @primary_category_id.setter
    def primary_category_id(self, primary_category_id):
        """Sets the primary_category_id of this Product.

        The identifier of the leaf category that eBay recommends using to list this product, based on previous listings of similar products. Products in the eBay catalog are not automatically associated with any particular category, but using an inappropriate category can make it difficult for prospective buyers to find the product. For other possible categories that might be used, see otherApplicableCategoryIds.  # noqa: E501

        :param primary_category_id: The primary_category_id of this Product.  # noqa: E501
        :type: str
        """

        self._primary_category_id = primary_category_id

    @property
    def product_web_url(self):
        """Gets the product_web_url of this Product.  # noqa: E501

        The URL for this product's eBay product page.  # noqa: E501

        :return: The product_web_url of this Product.  # noqa: E501
        :rtype: str
        """
        return self._product_web_url

    @product_web_url.setter
    def product_web_url(self, product_web_url):
        """Sets the product_web_url of this Product.

        The URL for this product's eBay product page.  # noqa: E501

        :param product_web_url: The product_web_url of this Product.  # noqa: E501
        :type: str
        """

        self._product_web_url = product_web_url

    @property
    def title(self):
        """Gets the title of this Product.  # noqa: E501

        The title of this product on eBay.  # noqa: E501

        :return: The title of this Product.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Product.

        The title of this product on eBay.  # noqa: E501

        :param title: The title of this Product.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def upc(self):
        """Gets the upc of this Product.  # noqa: E501

        A list of Universal Product Codes (UPCs) that identify this product.  # noqa: E501

        :return: The upc of this Product.  # noqa: E501
        :rtype: list[str]
        """
        return self._upc

    @upc.setter
    def upc(self, upc):
        """Sets the upc of this Product.

        A list of Universal Product Codes (UPCs) that identify this product.  # noqa: E501

        :param upc: The upc of this Product.  # noqa: E501
        :type: list[str]
        """

        self._upc = upc

    @property
    def version(self):
        """Gets the version of this Product.  # noqa: E501

        The current version number of this product record in the catalog.  # noqa: E501

        :return: The version of this Product.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Product.

        The current version number of this product record in the catalog.  # noqa: E501

        :param version: The version of this Product.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(Product, dict):
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
        if not isinstance(other, Product):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
