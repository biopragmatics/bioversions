# -*- coding: utf-8 -*-

"""A getter for MeSH."""

import ftplib

from bioversions.utils import Getter, VersionType

__all__ = [
    "MeshGetter",
]


class MeshGetter(Getter):
    """A getter for MeSH."""

    bioregistry_id = "mesh"
    name = "MeSH"
    homepage_fmt = "ftp://nlmpubs.nlm.nih.gov/online/mesh/{version}"
    version_type = VersionType.year

    def get(self):
        """Get the latest MeSH version number."""
        with ftplib.FTP("nlmpubs.nlm.nih.gov") as ftp:
            ftp.login()
            ftp.cwd("online/mesh/")
            versions = []
            for name, _ in ftp.mlsd():
                try:
                    int(name)
                except ValueError:
                    continue
                else:
                    versions.append(name)
            return max(versions)
        raise ValueError


if __name__ == "__main__":
    MeshGetter.print()
