# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CommitRelationshipsBuildsData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, type: str=None, id: int=None):  # noqa: E501
        """CommitRelationshipsBuildsData - a model defined in Swagger

        :param type: The type of this CommitRelationshipsBuildsData.  # noqa: E501
        :type type: str
        :param id: The id of this CommitRelationshipsBuildsData.  # noqa: E501
        :type id: int
        """
        self.swagger_types = {
            'type': str,
            'id': int
        }

        self.attribute_map = {
            'type': 'type',
            'id': 'id'
        }
        self._type = type
        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'CommitRelationshipsBuildsData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Commit_relationships_builds_data of this CommitRelationshipsBuildsData.  # noqa: E501
        :rtype: CommitRelationshipsBuildsData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this CommitRelationshipsBuildsData.


        :return: The type of this CommitRelationshipsBuildsData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this CommitRelationshipsBuildsData.


        :param type: The type of this CommitRelationshipsBuildsData.
        :type type: str
        """

        self._type = type

    @property
    def id(self) -> int:
        """Gets the id of this CommitRelationshipsBuildsData.


        :return: The id of this CommitRelationshipsBuildsData.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this CommitRelationshipsBuildsData.


        :param id: The id of this CommitRelationshipsBuildsData.
        :type id: int
        """

        self._id = id