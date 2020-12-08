# -*- coding: utf-8 -*-

"""Getters for OBO ontologies."""

from ..utils import OboGetter

__all__ = [
    'ChebiGetter',
    'GoGetter',
    'DoidGetter',
    'PrGetter',
    'XaoGetter',
]


class ChebiGetter(OboGetter):
    """A getter for ChEBI."""

    name = 'ChEBI'
    key = 'chebi'


class GoGetter(OboGetter):
    """A getter for the Gene Ontology (GO)."""

    name = 'Gene Ontology'
    key = 'go'
    strip_version_prefix = True


class DoidGetter(OboGetter):
    """A getter for the Disease Ontology (DO)."""

    name = 'Disease Ontology'
    homepage_fmt = 'https://github.com/DiseaseOntology/HumanDiseaseOntology/tree/main/src/ontology/releases/{version}'
    key = 'doid'
    strip_version_prefix = True
    strip_file_suffix = True


class PrGetter(OboGetter):
    """A getter for the Protein Ontology (PR)."""

    name = 'Protein Ontology'
    key = 'pr'


class XaoGetter(OboGetter):
    """A getter for the Xenopus Anatomy Ontology."""

    name = 'Xenopus Anatomy Ontology'
    key = 'xao'
    strip_version_prefix = True


if __name__ == '__main__':
    for _name, _cls in list(locals().items()):
        if _name.endswith('Getter') and hasattr(_cls, 'key'):
            _cls.print()
