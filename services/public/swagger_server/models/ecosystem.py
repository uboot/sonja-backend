# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.ecosystem_attributes import EcosystemAttributes  # noqa: F401,E501
from swagger_server.models.ecosystem_relationships import EcosystemRelationships  # noqa: F401,E501
from swagger_server import util


class Ecosystem(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, type: str=None, attributes: EcosystemAttributes=None, relationships: EcosystemRelationships=None):  # noqa: E501
        """Ecosystem - a model defined in Swagger

        :param id: The id of this Ecosystem.  # noqa: E501
        :type id: int
        :param type: The type of this Ecosystem.  # noqa: E501
        :type type: str
        :param attributes: The attributes of this Ecosystem.  # noqa: E501
        :type attributes: EcosystemAttributes
        :param relationships: The relationships of this Ecosystem.  # noqa: E501
        :type relationships: EcosystemRelationships
        """
        self.swagger_types = {
            'id': int,
            'type': str,
            'attributes': EcosystemAttributes,
            'relationships': EcosystemRelationships
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
    def from_dict(cls, dikt) -> 'Ecosystem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Ecosystem of this Ecosystem.  # noqa: E501
        :rtype: Ecosystem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Ecosystem.


        :return: The id of this Ecosystem.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Ecosystem.


        :param id: The id of this Ecosystem.
        :type id: int
        """

        self._id = id

    @property
    def type(self) -> str:
        """Gets the type of this Ecosystem.


        :return: The type of this Ecosystem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Ecosystem.


        :param type: The type of this Ecosystem.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def attributes(self) -> EcosystemAttributes:
        """Gets the attributes of this Ecosystem.


        :return: The attributes of this Ecosystem.
        :rtype: EcosystemAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes: EcosystemAttributes):
        """Sets the attributes of this Ecosystem.


        :param attributes: The attributes of this Ecosystem.
        :type attributes: EcosystemAttributes
        """

        self._attributes = attributes

    @property
    def relationships(self) -> EcosystemRelationships:
        """Gets the relationships of this Ecosystem.


        :return: The relationships of this Ecosystem.
        :rtype: EcosystemRelationships
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships: EcosystemRelationships):
        """Sets the relationships of this Ecosystem.


        :param relationships: The relationships of this Ecosystem.
        :type relationships: EcosystemRelationships
        """

        self._relationships = relationships
