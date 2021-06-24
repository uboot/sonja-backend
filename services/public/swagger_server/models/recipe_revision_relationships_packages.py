# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.build_relationships_package_data import BuildRelationshipsPackageData  # noqa: F401,E501
from swagger_server import util


class RecipeRevisionRelationshipsPackages(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, data: List[BuildRelationshipsPackageData]=None):  # noqa: E501
        """RecipeRevisionRelationshipsPackages - a model defined in Swagger

        :param data: The data of this RecipeRevisionRelationshipsPackages.  # noqa: E501
        :type data: List[BuildRelationshipsPackageData]
        """
        self.swagger_types = {
            'data': List[BuildRelationshipsPackageData]
        }

        self.attribute_map = {
            'data': 'data'
        }
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'RecipeRevisionRelationshipsPackages':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RecipeRevision_relationships_packages of this RecipeRevisionRelationshipsPackages.  # noqa: E501
        :rtype: RecipeRevisionRelationshipsPackages
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> List[BuildRelationshipsPackageData]:
        """Gets the data of this RecipeRevisionRelationshipsPackages.


        :return: The data of this RecipeRevisionRelationshipsPackages.
        :rtype: List[BuildRelationshipsPackageData]
        """
        return self._data

    @data.setter
    def data(self, data: List[BuildRelationshipsPackageData]):
        """Sets the data of this RecipeRevisionRelationshipsPackages.


        :param data: The data of this RecipeRevisionRelationshipsPackages.
        :type data: List[BuildRelationshipsPackageData]
        """

        self._data = data