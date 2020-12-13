# -*- coding: utf-8 -*-

"""Getters for OBO ontologies."""

from ..utils import OboGetter

__all__ = [
    'ChebiGetter',
    'ClGetter',
    'GoGetter',
    'DoidGetter',
    'PatoGetter',
    'PoGetter',
    'PrGetter',
    'XaoGetter',
    'ZfaGetter',
]


class ChebiGetter(OboGetter):
    """A getter for ChEBI."""

    name = 'ChEBI'
    key = 'chebi'


class ClGetter(OboGetter):
    """A getter for the Cell Ontology (cl)."""

    name = 'Cell Ontology'
    key = 'cl'
    strip_version_prefix = True


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


class PatoGetter(OboGetter):
    """A getter for the Phenotype and Trait Ontology (PATO)."""

    name = 'Phenotype And Trait Ontology '
    key = 'pato'
    strip_version_prefix = True
    strip_file_suffix = True


class PoGetter(OboGetter):
    """A getter for the Plant Ontology (PO)."""

    name = 'Plant Ontology'
    key = 'po'
    strip_version_prefix = True


class PrGetter(OboGetter):
    """A getter for the Protein Ontology (PR)."""

    name = 'Protein Ontology'
    key = 'pr'


class XaoGetter(OboGetter):
    """A getter for the Xenopus Anatomy Ontology."""

    name = 'Xenopus Anatomy Ontology'
    key = 'xao'
    strip_version_prefix = True


class ZfaGetter(OboGetter):
    """A getter for the Zebrafish anatomy and development ontology (ZFA)."""

    name = 'Zebrafish anatomy and development ontology'
    key = 'zfa'
    strip_version_prefix = True


if __name__ == '__main__':
    for _name, _cls in list(locals().items()):
        if _name.endswith('Getter') and hasattr(_cls, 'key'):
            _cls.print()
