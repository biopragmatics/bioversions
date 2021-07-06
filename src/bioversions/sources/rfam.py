# -*- coding: utf-8 -*-

"""A getter for Rfam."""

from bioversions.utils import Getter, VersionType, _get_ftp_version

__all__ = [
    "RfamGetter",
]


class RfamGetter(Getter):
    """A getter for Rfam."""

    bioregistry_id = "rfam"
    name = "Rfam"
    homepage_fmt = "ftp://ftp.ebi.ac.uk/pub/databases/Rfam/{version}/"
    version_type = VersionType.semver_minor

    def get(self):
        """Get the latest Rfam version number."""
        return _get_ftp_version("ftp.ebi.ac.uk", "pub/databases/Rfam/")


if __name__ == "__main__":
    RfamGetter.print()
