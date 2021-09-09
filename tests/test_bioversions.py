# -*- coding: utf-8 -*-

"""Tests for bioversions."""

import datetime
import unittest
from collections import Counter

from tabulate import tabulate

import bioversions
from bioversions.resources import load_versions
from bioversions.sources import BioGRIDGetter, WikiPathwaysGetter


class TestData(unittest.TestCase):
    """Tests for the data."""

    def test_duplicates(self):
        """Test there are no duplicate prefixes."""
        versions = load_versions()
        counter = Counter(
            entry["prefix"]
            for entry in versions["database"]
            if entry.get("prefix")
        )
        duplicates = {
            prefix: count
            for prefix, count in counter.items()
            if count > 1
        }
        if duplicates:
            t = tabulate(duplicates.items(), headers=["Prefix", "Count"])
            self.fail(f"Found duplicates for {len(duplicates)} prefixes:\n\n{t}")


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
