# -*- coding: utf-8 -*-

"""Getters for OBO ontologies."""

from ..utils import OboGetter

__all__ = [
    'ChebiGetter',
    'ClGetter',
    'GoGetter',
    'DoidGetter',
    'HpGetter',
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
    homepage_fmt = 'ftp://ftp.ebi.ac.uk/pub/databases/chebi/archive/rel{version}/'


class ClGetter(OboGetter):
    """A getter for the Cell Ontology (cl)."""

    name = 'Cell Ontology'
    key = 'cl'
    strip_version_prefix = True
    date_version_fmt = '%Y-%m-%d'


class GoGetter(OboGetter):
    """A getter for the Gene Ontology (GO)."""

    name = 'Gene Ontology'
    key = 'go'
    strip_version_prefix = True
    date_version_fmt = '%Y-%m-%d'
    homepage_fmt = 'http://archive.geneontology.org/full/{version}/'


class DoidGetter(OboGetter):
    """A getter for the Disease Ontology (DO)."""

    name = 'Disease Ontology'
    homepage_fmt = 'https://github.com/DiseaseOntology/HumanDiseaseOntology/tree/main/src/ontology/releases/{version}'
    key = 'doid'
    strip_version_prefix = True
    strip_file_suffix = True
    date_version_fmt = '%Y-%m-%d'


class HpGetter(OboGetter):
    """A getter for the Human Phenotype Ontology (HP)."""

    name = 'Human Phenotype Ontology'
    key = 'hp'
    strip_key_prefix = True
    strip_version_prefix = True
    date_version_fmt = '%Y-%m-%d'


class PatoGetter(OboGetter):
    """A getter for the Phenotype and Trait Ontology (PATO)."""

    name = 'Phenotype And Trait Ontology'
    key = 'pato'
    strip_version_prefix = True
    strip_file_suffix = True
    date_version_fmt = '%Y-%m-%d'


class PoGetter(OboGetter):
    """A getter for the Plant Ontology (PO)."""

    name = 'Plant Ontology'
    key = 'po'
    strip_version_prefix = True
    date_version_fmt = '%Y-%m-%d'


class PrGetter(OboGetter):
    """A getter for the Protein Ontology (PR)."""

    name = 'Protein Ontology'
    key = 'pr'
    homepage_fmt = 'https://proconsortium.org/download/release_{version}/'


class XaoGetter(OboGetter):
    """A getter for the Xenopus Anatomy Ontology."""

    name = 'Xenopus Anatomy Ontology'
    key = 'xao'
    strip_version_prefix = True
    date_version_fmt = '%Y-%m-%d'


class ZfaGetter(OboGetter):
    """A getter for the Zebrafish anatomy and development ontology (ZFA)."""

    name = 'Zebrafish anatomy and development ontology'
    key = 'zfa'
    strip_version_prefix = True
    date_version_fmt = '%Y-%m-%d'


if __name__ == '__main__':
    for _name, _cls in list(locals().items()):
        if _name.endswith('Getter') and hasattr(_cls, 'key'):
            _cls.print()
