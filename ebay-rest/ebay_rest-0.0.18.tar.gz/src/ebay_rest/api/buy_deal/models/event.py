# coding: utf-8

"""
    Deal API

    <span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br /><br />This API allows third-party developers to search for and retrieve details about eBay deals and events, as well as the items associated with those deals and events.  # noqa: E501

    OpenAPI spec version: v1.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Event(object):
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
        'applicable_coupons': 'list[Coupon]',
        'description': 'str',
        'end_date': 'str',
        'event_affiliate_web_url': 'str',
        'event_id': 'str',
        'event_web_url': 'str',
        'images': 'list[Image]',
        'start_date': 'str',
        'terms': 'Terms',
        'title': 'str'
    }

    attribute_map = {
        'applicable_coupons': 'applicableCoupons',
        'description': 'description',
        'end_date': 'endDate',
        'event_affiliate_web_url': 'eventAffiliateWebUrl',
        'event_id': 'eventId',
        'event_web_url': 'eventWebUrl',
        'images': 'images',
        'start_date': 'startDate',
        'terms': 'terms',
        'title': 'title'
    }

    def __init__(self, applicable_coupons=None, description=None, end_date=None, event_affiliate_web_url=None, event_id=None, event_web_url=None, images=None, start_date=None, terms=None, title=None):  # noqa: E501
        """Event - a model defined in Swagger"""  # noqa: E501
        self._applicable_coupons = None
        self._description = None
        self._end_date = None
        self._event_affiliate_web_url = None
        self._event_id = None
        self._event_web_url = None
        self._images = None
        self._start_date = None
        self._terms = None
        self._title = None
        self.discriminator = None
        if applicable_coupons is not None:
            self.applicable_coupons = applicable_coupons
        if description is not None:
            self.description = description
        if end_date is not None:
            self.end_date = end_date
        if event_affiliate_web_url is not None:
            self.event_affiliate_web_url = event_affiliate_web_url
        if event_id is not None:
            self.event_id = event_id
        if event_web_url is not None:
            self.event_web_url = event_web_url
        if images is not None:
            self.images = images
        if start_date is not None:
            self.start_date = start_date
        if terms is not None:
            self.terms = terms
        if title is not None:
            self.title = title

    @property
    def applicable_coupons(self):
        """Gets the applicable_coupons of this Event.  # noqa: E501

        A list of coupons associated with the event.  # noqa: E501

        :return: The applicable_coupons of this Event.  # noqa: E501
        :rtype: list[Coupon]
        """
        return self._applicable_coupons

    @applicable_coupons.setter
    def applicable_coupons(self, applicable_coupons):
        """Sets the applicable_coupons of this Event.

        A list of coupons associated with the event.  # noqa: E501

        :param applicable_coupons: The applicable_coupons of this Event.  # noqa: E501
        :type: list[Coupon]
        """

        self._applicable_coupons = applicable_coupons

    @property
    def description(self):
        """Gets the description of this Event.  # noqa: E501

        The event description.  # noqa: E501

        :return: The description of this Event.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Event.

        The event description.  # noqa: E501

        :param description: The description of this Event.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def end_date(self):
        """Gets the end_date of this Event.  # noqa: E501

        The end date for the event.  # noqa: E501

        :return: The end_date of this Event.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Event.

        The end date for the event.  # noqa: E501

        :param end_date: The end_date of this Event.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def event_affiliate_web_url(self):
        """Gets the event_affiliate_web_url of this Event.  # noqa: E501

        The URL of the View Event page for the event, which includes the affiliate tracking ID.  # noqa: E501

        :return: The event_affiliate_web_url of this Event.  # noqa: E501
        :rtype: str
        """
        return self._event_affiliate_web_url

    @event_affiliate_web_url.setter
    def event_affiliate_web_url(self, event_affiliate_web_url):
        """Sets the event_affiliate_web_url of this Event.

        The URL of the View Event page for the event, which includes the affiliate tracking ID.  # noqa: E501

        :param event_affiliate_web_url: The event_affiliate_web_url of this Event.  # noqa: E501
        :type: str
        """

        self._event_affiliate_web_url = event_affiliate_web_url

    @property
    def event_id(self):
        """Gets the event_id of this Event.  # noqa: E501

        The unique identifier for the event.  # noqa: E501

        :return: The event_id of this Event.  # noqa: E501
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this Event.

        The unique identifier for the event.  # noqa: E501

        :param event_id: The event_id of this Event.  # noqa: E501
        :type: str
        """

        self._event_id = event_id

    @property
    def event_web_url(self):
        """Gets the event_web_url of this Event.  # noqa: E501

        The web URL for the event.  # noqa: E501

        :return: The event_web_url of this Event.  # noqa: E501
        :rtype: str
        """
        return self._event_web_url

    @event_web_url.setter
    def event_web_url(self, event_web_url):
        """Sets the event_web_url of this Event.

        The web URL for the event.  # noqa: E501

        :param event_web_url: The event_web_url of this Event.  # noqa: E501
        :type: str
        """

        self._event_web_url = event_web_url

    @property
    def images(self):
        """Gets the images of this Event.  # noqa: E501

        The images for the event.  # noqa: E501

        :return: The images of this Event.  # noqa: E501
        :rtype: list[Image]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this Event.

        The images for the event.  # noqa: E501

        :param images: The images of this Event.  # noqa: E501
        :type: list[Image]
        """

        self._images = images

    @property
    def start_date(self):
        """Gets the start_date of this Event.  # noqa: E501

        The start date for the event.  # noqa: E501

        :return: The start_date of this Event.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Event.

        The start date for the event.  # noqa: E501

        :param start_date: The start_date of this Event.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def terms(self):
        """Gets the terms of this Event.  # noqa: E501


        :return: The terms of this Event.  # noqa: E501
        :rtype: Terms
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """Sets the terms of this Event.


        :param terms: The terms of this Event.  # noqa: E501
        :type: Terms
        """

        self._terms = terms

    @property
    def title(self):
        """Gets the title of this Event.  # noqa: E501

        The title of the event.  # noqa: E501

        :return: The title of this Event.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Event.

        The title of the event.  # noqa: E501

        :param title: The title of this Event.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(Event, dict):
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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
