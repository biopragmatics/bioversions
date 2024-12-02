"""Getters for OBO ontologies."""

from collections.abc import Iterable

from bioversions.utils import Getter, OBOFoundryGetter, VersionType

__all__ = [
    "ChebiGetter",
    "DoidGetter",
    "GoGetter",
    "PrGetter",
    "iter_obo_getters",
]


class ChebiGetter(OBOFoundryGetter):
    """A getter for ChEBI."""

    name = "ChEBI"
    bioregistry_id = "chebi"
    version_type = VersionType.sequential
    homepage_fmt = "ftp://ftp.ebi.ac.uk/pub/databases/chebi/archive/rel{version}/"


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


class PrGetter(OBOFoundryGetter):
    """A getter for the Protein Ontology (PR)."""

    name = "Protein Ontology"
    bioregistry_id = "pr"
    version_type = VersionType.semver_minor
    homepage_fmt = "https://proconsortium.org/download/release_{version}/"


def iter_obo_getters() -> Iterable[type[Getter]]:
    """Iterate over OBO getters."""
    yield from OBOFoundryGetter.__subclasses__()


def _main():
    for getter in iter_obo_getters():
        getter.print()


if __name__ == "__main__":
    _main()
