# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.build_relationships_missingpackages import BuildRelationshipsMissingpackages  # noqa: F401,E501
from swagger_server.models.package_relationships_reciperevision import PackageRelationshipsReciperevision  # noqa: F401,E501
from swagger_server import util


class PackageRelationships(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, recipe_revision: PackageRelationshipsReciperevision=None, requires: BuildRelationshipsMissingpackages=None, required_by: BuildRelationshipsMissingpackages=None):  # noqa: E501
        """PackageRelationships - a model defined in Swagger

        :param recipe_revision: The recipe_revision of this PackageRelationships.  # noqa: E501
        :type recipe_revision: PackageRelationshipsReciperevision
        :param requires: The requires of this PackageRelationships.  # noqa: E501
        :type requires: BuildRelationshipsMissingpackages
        :param required_by: The required_by of this PackageRelationships.  # noqa: E501
        :type required_by: BuildRelationshipsMissingpackages
        """
        self.swagger_types = {
            'recipe_revision': PackageRelationshipsReciperevision,
            'requires': BuildRelationshipsMissingpackages,
            'required_by': BuildRelationshipsMissingpackages
        }

        self.attribute_map = {
            'recipe_revision': 'recipe-revision',
            'requires': 'requires',
            'required_by': 'required-by'
        }
        self._recipe_revision = recipe_revision
        self._requires = requires
        self._required_by = required_by

    @classmethod
    def from_dict(cls, dikt) -> 'PackageRelationships':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Package_relationships of this PackageRelationships.  # noqa: E501
        :rtype: PackageRelationships
        """
        return util.deserialize_model(dikt, cls)

    @property
    def recipe_revision(self) -> PackageRelationshipsReciperevision:
        """Gets the recipe_revision of this PackageRelationships.


        :return: The recipe_revision of this PackageRelationships.
        :rtype: PackageRelationshipsReciperevision
        """
        return self._recipe_revision

    @recipe_revision.setter
    def recipe_revision(self, recipe_revision: PackageRelationshipsReciperevision):
        """Sets the recipe_revision of this PackageRelationships.


        :param recipe_revision: The recipe_revision of this PackageRelationships.
        :type recipe_revision: PackageRelationshipsReciperevision
        """

        self._recipe_revision = recipe_revision

    @property
    def requires(self) -> BuildRelationshipsMissingpackages:
        """Gets the requires of this PackageRelationships.


        :return: The requires of this PackageRelationships.
        :rtype: BuildRelationshipsMissingpackages
        """
        return self._requires

    @requires.setter
    def requires(self, requires: BuildRelationshipsMissingpackages):
        """Sets the requires of this PackageRelationships.


        :param requires: The requires of this PackageRelationships.
        :type requires: BuildRelationshipsMissingpackages
        """

        self._requires = requires

    @property
    def required_by(self) -> BuildRelationshipsMissingpackages:
        """Gets the required_by of this PackageRelationships.


        :return: The required_by of this PackageRelationships.
        :rtype: BuildRelationshipsMissingpackages
        """
        return self._required_by

    @required_by.setter
    def required_by(self, required_by: BuildRelationshipsMissingpackages):
        """Sets the required_by of this PackageRelationships.


        :param required_by: The required_by of this PackageRelationships.
        :type required_by: BuildRelationshipsMissingpackages
        """

        self._required_by = required_by