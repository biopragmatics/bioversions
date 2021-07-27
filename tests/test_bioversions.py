# -*- coding: utf-8 -*-

"""Tests for bioversions."""

import datetime
import unittest

import bioversions
from bioversions.sources import BioGRIDGetter, WikiPathwaysGetter


class TestGetter(unittest.TestCase):
    """Tests for the Getter class."""

    def test_get(self):
        """Test getters."""
        prefixes = [
            "reactome",
            "kegg",
        ]
        for prefix in prefixes:
            with self.subTest(prefix=prefix):
                s = bioversions.get_version(prefix)
                self.assertIsInstance(s, str)

    def test_getter(self):
        """Test the BioGRID getter."""
        s = BioGRIDGetter.version
        self.assertIsInstance(s, str)

    def test_date(self):
        """Test getters that have versions as dates."""
        for getter in [WikiPathwaysGetter]:
            with self.subTest(getter=getter.name):
                s = getter.version
                self.assertIsInstance(s, str)

                d = getter.version_date_parsed
                self.assertIsInstance(d, datetime.date)
