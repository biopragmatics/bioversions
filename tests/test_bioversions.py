"""Tests for bioversions."""

import datetime
import re
import unittest

import bioregistry

import bioversions
from bioversions.sources import BioGRIDGetter, WikiPathwaysGetter, get_getters
from bioversions.utils import get_obo_version, get_obograph_json_version, get_owl_xml_version

YYYYMMDD = re.compile("\\d{4}-\\d{2}-\\d{2}")


class TestGetter(unittest.TestCase):
    """Tests for the Getter class."""

    def test_bioregistry_ids(self) -> None:
        """Test Bioregistry prefixes are all canonical."""
        prefixes = set(bioregistry.read_registry())
        for getter in get_getters():
            if getter.bioregistry_id is None:
                continue
            with self.subTest(name=getter.name):
                self.assertIn(getter.bioregistry_id, prefixes)

    def test_get(self) -> None:
        """Test getters."""
        prefixes = [
            "reactome",
            "kegg",
        ]
        for prefix in prefixes:
            with self.subTest(prefix=prefix):
                s = bioversions.get_version(prefix)
                self.assertIsInstance(s, str)

    def test_getter(self) -> None:
        """Test the BioGRID getter."""
        s = BioGRIDGetter.version
        self.assertIsInstance(s, str)

    def test_date(self) -> None:
        """Test getters that have versions as dates."""
        for getter in [WikiPathwaysGetter]:
            with self.subTest(getter=getter.name):
                s = getter.version
                self.assertIsInstance(s, str)

                d = getter.version_date_parsed
                self.assertIsInstance(d, datetime.date)

    def test_get_obo_version(self) -> None:
        """Test getting an OBO version."""
        version = get_obo_version("https://current.geneontology.org/ontology/go.obo")
        if version is None:
            raise ValueError
        version = version.removeprefix("releases/")
        self.assertRegex(version, YYYYMMDD)

    def test_get_obograph_version(self) -> None:
        """Test getting an OBO graph version."""
        version = get_obograph_json_version("http://purl.obolibrary.org/obo/go.json")
        self.assertRegex(_clean_owl(version), YYYYMMDD)

    def test_get_owl_xml_version(self) -> None:
        """Test getting an OWL XML version."""
        version = get_owl_xml_version("https://current.geneontology.org/ontology/go.owl")
        self.assertRegex(_clean_owl(version), YYYYMMDD)


def _clean_owl(version: str | None) -> str:
    if version is None:
        raise ValueError
    return (
        version.strip('"')
        .removeprefix("http://purl.obolibrary.org/obo/go/releases/")
        .removesuffix("/go.owl")
    )
