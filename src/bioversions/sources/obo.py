"""Getters for OBO ontologies."""

from bioversions.utils import OBOFoundryGetter, VersionType

__all__ = [
    "DoidGetter",
    "GoGetter",
]


class GoGetter(OBOFoundryGetter):
    """A getter for the Gene Ontology (GO)."""

    name = "Gene Ontology"
    bioregistry_id = "go"
    version_type = VersionType.date
    strip_version_prefix = True
    date_version_fmt = "%Y-%m-%d"
    homepage_fmt = "http://archive.geneontology.org/full/{version}/"


class DoidGetter(OBOFoundryGetter):
    """A getter for the Disease Ontology (DO)."""

    name = "Disease Ontology"
    homepage_fmt = "https://github.com/DiseaseOntology/HumanDiseaseOntology/tree/main/src/ontology/releases/{version}"
    bioregistry_id = "doid"
    version_type = VersionType.date
    strip_version_prefix = True
    strip_file_suffix = True
    date_version_fmt = "%Y-%m-%d"
