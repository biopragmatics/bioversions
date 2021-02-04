# -*- coding: utf-8 -*-

"""Tests for bioversions."""

import datetime
import unittest

from bioversions.sources import BioGRIDGetter, WikiPathwaysGetter


class TestGetter(unittest.TestCase):
    """Tests for the Getter class."""

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
