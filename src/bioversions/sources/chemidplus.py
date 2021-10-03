# -*- coding: utf-8 -*-

"""A getter for ChemIDplus."""

import re

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "ChemIDplusGetter",
]


class ChemIDplusGetter(Getter):
    """A getter for ChemIDplus."""

    bioregistry_id = "chemidplus"
    name = "ChemIDplus"
    date_version_fmt = "%Y-%m-%d"
    homepage_fmt = "https://ftp.nlm.nih.gov/projects/chemidlease/chem.xml.{version}.zip"
    version_type = VersionType.date

    def get(self):
        """Get the latest ChemIDplus version number."""
        latest_url = "https://ftp.nlm.nih.gov/projects/chemidlease/CurrentChemID.xml"
        headers = {"Range": "bytes=0-300"}  # leave some slack to capture date
        r = requests.get(latest_url, headers=headers)
        if r.status_code == 206:
            result = re.search(r" date=\"([0-9]{4}-[0-9]{2}-[0-9]{2})\">", r.text)
            if result:
                return result.groups()[0]
        raise ValueError

    @staticmethod
    def homepage_version_transform(version: str) -> str:
        """Replace dots with dashes for ChemIDplus homepage format."""
        return version.replace("-", "")


if __name__ == "__main__":
    ChemIDplusGetter.print()
