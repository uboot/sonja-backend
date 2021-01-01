# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.build_attributes import BuildAttributes  # noqa: F401,E501
from swagger_server.models.build_relationships import BuildRelationships  # noqa: F401,E501
from swagger_server import util


class Build(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, type: str=None, attributes: BuildAttributes=None, relationships: BuildRelationships=None):  # noqa: E501
        """Build - a model defined in Swagger

        :param id: The id of this Build.  # noqa: E501
        :type id: int
        :param type: The type of this Build.  # noqa: E501
        :type type: str
        :param attributes: The attributes of this Build.  # noqa: E501
        :type attributes: BuildAttributes
        :param relationships: The relationships of this Build.  # noqa: E501
        :type relationships: BuildRelationships
        """
        self.swagger_types = {
            'id': int,
            'type': str,
            'attributes': BuildAttributes,
            'relationships': BuildRelationships
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'attributes': 'attributes',
            'relationships': 'relationships'
        }
        self._id = id
        self._type = type
        self._attributes = attributes
        self._relationships = relationships

    @classmethod
    def from_dict(cls, dikt) -> 'Build':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Build of this Build.  # noqa: E501
        :rtype: Build
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Build.


        :return: The id of this Build.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Build.


        :param id: The id of this Build.
        :type id: int
        """

        self._id = id

    @property
    def type(self) -> str:
        """Gets the type of this Build.


        :return: The type of this Build.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Build.


        :param type: The type of this Build.
        :type type: str
        """

        self._type = type

    @property
    def attributes(self) -> BuildAttributes:
        """Gets the attributes of this Build.


        :return: The attributes of this Build.
        :rtype: BuildAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes: BuildAttributes):
        """Sets the attributes of this Build.


        :param attributes: The attributes of this Build.
        :type attributes: BuildAttributes
        """

        self._attributes = attributes

    @property
    def relationships(self) -> BuildRelationships:
        """Gets the relationships of this Build.


        :return: The relationships of this Build.
        :rtype: BuildRelationships
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships: BuildRelationships):
        """Sets the relationships of this Build.


        :param relationships: The relationships of this Build.
        :type relationships: BuildRelationships
        """

        self._relationships = relationships
