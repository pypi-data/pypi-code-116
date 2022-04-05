# coding: utf-8

"""
    ARLAS Exploration API

    Explore the content of ARLAS collections  # noqa: E501

    OpenAPI spec version: 21.0.0
    Contact: contact@gisaia.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Feature(object):
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
        'crs': 'Crs',
        'bbox': 'list[float]',
        'properties': 'dict(str, object)',
        'geometry': 'object',
        'id': 'str'
    }

    attribute_map = {
        'crs': 'crs',
        'bbox': 'bbox',
        'properties': 'properties',
        'geometry': 'geometry',
        'id': 'id'
    }

    def __init__(self, crs=None, bbox=None, properties=None, geometry=None, id=None):  # noqa: E501
        """Feature - a model defined in Swagger"""  # noqa: E501

        self._crs = None
        self._bbox = None
        self._properties = None
        self._geometry = None
        self._id = None
        self.discriminator = None

        if crs is not None:
            self.crs = crs
        if bbox is not None:
            self.bbox = bbox
        if properties is not None:
            self.properties = properties
        if geometry is not None:
            self.geometry = geometry
        if id is not None:
            self.id = id

    @property
    def crs(self):
        """Gets the crs of this Feature.  # noqa: E501


        :return: The crs of this Feature.  # noqa: E501
        :rtype: Crs
        """
        return self._crs

    @crs.setter
    def crs(self, crs):
        """Sets the crs of this Feature.


        :param crs: The crs of this Feature.  # noqa: E501
        :type: Crs
        """

        self._crs = crs

    @property
    def bbox(self):
        """Gets the bbox of this Feature.  # noqa: E501


        :return: The bbox of this Feature.  # noqa: E501
        :rtype: list[float]
        """
        return self._bbox

    @bbox.setter
    def bbox(self, bbox):
        """Sets the bbox of this Feature.


        :param bbox: The bbox of this Feature.  # noqa: E501
        :type: list[float]
        """

        self._bbox = bbox

    @property
    def properties(self):
        """Gets the properties of this Feature.  # noqa: E501


        :return: The properties of this Feature.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Feature.


        :param properties: The properties of this Feature.  # noqa: E501
        :type: dict(str, object)
        """

        self._properties = properties

    @property
    def geometry(self):
        """Gets the geometry of this Feature.  # noqa: E501


        :return: The geometry of this Feature.  # noqa: E501
        :rtype: object
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this Feature.


        :param geometry: The geometry of this Feature.  # noqa: E501
        :type: object
        """

        self._geometry = geometry

    @property
    def id(self):
        """Gets the id of this Feature.  # noqa: E501


        :return: The id of this Feature.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Feature.


        :param id: The id of this Feature.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(Feature, dict):
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
        if not isinstance(other, Feature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
