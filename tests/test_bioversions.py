# -*- coding: utf-8 -*-

"""Tests for bioversions."""

import unittest

from bioversions.sources.biogrid import BioGRIDGetter


class TestGetter(unittest.TestCase):
    """Tests for the Getter class."""

    def test_getter(self):
        """Test the BioGRID getter."""
        s = BioGRIDGetter.version
        self.assertIsInstance(s, str)
