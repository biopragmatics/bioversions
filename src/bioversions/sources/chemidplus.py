# -*- coding: utf-8 -*-

"""A getter for ChemIDplus."""

import re

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "ChemIDplusGetter",
]

RELEASE_PREFIX = "* Release:"
DATE_PREFIX = "* Date:"


class ChemIDplusGetter(Getter):
    """A getter for ChemIDplus."""

    bioregistry_id = "chemidplus"
    name = "ChemIDplus"
    homepage_fmt = "https://ftp.nlm.nih.gov/projects/chemidlease/chem.xm.{version}.zip"
    version_type = VersionType.date

    def get(self):
        """Get the latest ChemIDplus version number."""
        latest_url = "https://ftp.nlm.nih.gov/projects/chemidlease/CurrentChemID.xml"
        headers = {"Range": "bytes=0-300"}  # leave some slack to capture date
        r = requests.get(latest_url, headers=headers)
        print(r.status_code)
        if r.status_code == 206:
            result = re.search(r" date=\"([0-9]{4}-[0-9]{2}-[0-9]{2})\">", r.text)
            if result:
                return result.groups()[0]


if __name__ == "__main__":
    ChemIDplusGetter.print()
