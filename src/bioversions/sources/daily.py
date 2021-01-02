# -*- coding: utf-8 -*-

"""A collection of daily updated resources that aren't assigned specific versions."""

from bioversions.utils import DailyGetter


class NCBIGeneGetter(DailyGetter):
    """A getter for NCBI Gene."""

    name = 'NCBI Gene'
