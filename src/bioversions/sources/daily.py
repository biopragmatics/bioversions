"""A collection of daily updated resources that aren't assigned specific versions."""

from bioversions.utils import DailyGetter


class NCBIGeneGetter(DailyGetter):
    """A getter for NCBI Gene."""

    bioregistry_id = "ncbigene"
    name = "NCBI Gene"
