# -*- coding: utf-8 -*-

"""A getter for Rhea."""

import requests
import requests_ftp

from bioversions.utils import Getter, VersionType

__all__ = [
    "RheaGetter",
]

requests_ftp.monkeypatch_session()

VERSION_FILE = "ftp://ftp.expasy.org/databases/rhea/rhea-release.properties"


class RheaGetter(Getter):
    """A getter for Rhea."""

    bioregistry_id = "rhea"
    name = "Rhea"
    date_fmt = "%Y-%m-%d"
    version_type = VersionType.date

    def get(self):
        """Get the latest Rhea version number."""
        with requests.Session() as session:
            res = session.get(VERSION_FILE)
            d = dict(line.strip().split("=") for line in res.text.splitlines() if line.strip())
        return {
            "version": d["rhea.release.number"],
            "date": d["rhea.release.date"],
        }


if __name__ == "__main__":
    RheaGetter.print()
