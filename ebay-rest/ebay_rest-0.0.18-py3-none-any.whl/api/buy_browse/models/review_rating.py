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

class ReviewRating(object):
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
        'average_rating': 'str',
        'rating_histograms': 'list[RatingHistogram]',
        'review_count': 'int'
    }

    attribute_map = {
        'average_rating': 'averageRating',
        'rating_histograms': 'ratingHistograms',
        'review_count': 'reviewCount'
    }

    def __init__(self, average_rating=None, rating_histograms=None, review_count=None):  # noqa: E501
        """ReviewRating - a model defined in Swagger"""  # noqa: E501
        self._average_rating = None
        self._rating_histograms = None
        self._review_count = None
        self.discriminator = None
        if average_rating is not None:
            self.average_rating = average_rating
        if rating_histograms is not None:
            self.rating_histograms = rating_histograms
        if review_count is not None:
            self.review_count = review_count

    @property
    def average_rating(self):
        """Gets the average_rating of this ReviewRating.  # noqa: E501

        The average rating given to a product based on customer reviews.  # noqa: E501

        :return: The average_rating of this ReviewRating.  # noqa: E501
        :rtype: str
        """
        return self._average_rating

    @average_rating.setter
    def average_rating(self, average_rating):
        """Sets the average_rating of this ReviewRating.

        The average rating given to a product based on customer reviews.  # noqa: E501

        :param average_rating: The average_rating of this ReviewRating.  # noqa: E501
        :type: str
        """

        self._average_rating = average_rating

    @property
    def rating_histograms(self):
        """Gets the rating_histograms of this ReviewRating.  # noqa: E501

        An array of containers for the product rating histograms that shows the review counts and the product rating.  # noqa: E501

        :return: The rating_histograms of this ReviewRating.  # noqa: E501
        :rtype: list[RatingHistogram]
        """
        return self._rating_histograms

    @rating_histograms.setter
    def rating_histograms(self, rating_histograms):
        """Sets the rating_histograms of this ReviewRating.

        An array of containers for the product rating histograms that shows the review counts and the product rating.  # noqa: E501

        :param rating_histograms: The rating_histograms of this ReviewRating.  # noqa: E501
        :type: list[RatingHistogram]
        """

        self._rating_histograms = rating_histograms

    @property
    def review_count(self):
        """Gets the review_count of this ReviewRating.  # noqa: E501

        The total number of reviews for the item.  # noqa: E501

        :return: The review_count of this ReviewRating.  # noqa: E501
        :rtype: int
        """
        return self._review_count

    @review_count.setter
    def review_count(self, review_count):
        """Sets the review_count of this ReviewRating.

        The total number of reviews for the item.  # noqa: E501

        :param review_count: The review_count of this ReviewRating.  # noqa: E501
        :type: int
        """

        self._review_count = review_count

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
        if issubclass(ReviewRating, dict):
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
        if not isinstance(other, ReviewRating):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
