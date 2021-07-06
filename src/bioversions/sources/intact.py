# -*- coding: utf-8 -*-

"""A getter for IntAct."""

from bioversions.utils import Getter, VersionType, _get_ftp_date_version

__all__ = [
    "IntActGetter",
]


class IntActGetter(Getter):
    """A getter for IntAct."""

    bioregistry_id = "intact"
    name = "IntAct"
    homepage_fmt = "ftp://ftp.ebi.ac.uk/pub/databases/intact/{version}/"
    date_version_fmt = "%Y-%m-%d"
    version_type = VersionType.date

    def get(self):
        """Get the latest IntAct version number."""
        return _get_ftp_date_version("ftp.ebi.ac.uk", "pub/databases/intact/")


if __name__ == "__main__":
    IntActGetter.print()
