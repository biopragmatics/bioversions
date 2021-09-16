# -*- coding: utf-8 -*-

"""A getter for SGD."""

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "SgdGetter",
]

VERSION_FILE = (
    "http://sgd-archive.yeastgenome.org/sequence/S288C_reference/dates_of_genome_releases.tab"
)


class SgdGetter(Getter):
    """A getter for SGD."""

    bioregistry_id = "sgd"
    name = "Saccharomyces Genome Database"
    date_fmt = "%Y-%m-%d"
    version_type = VersionType.date

    def get(self):
        """Get the latest SGD version number."""
        with requests.Session() as session:
            res = session.get(VERSION_FILE)
            d = dict(line.strip().split("\t") for line in res.text.splitlines() if line.strip())
        version = max(d, key=d.get)
        return {
            "version": version,
            "date": d[version],
        }


if __name__ == "__main__":
    SgdGetter.print()
