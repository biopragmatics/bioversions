# -*- coding: utf-8 -*-

"""A getter for SwissLipids."""

import datetime

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "SwissLipidGetter",
]


class SwissLipidGetter(Getter):
    """A getter for SwissLipids."""

    bioregistry_id = "slm"
    name = "SwissLipids"
    version_type = VersionType.date

    def get(self):
        """Get the latest SwissLipids version number."""
        res = requests.get("https://www.swisslipids.org/api/downloadData").json()
        record = next(record for record in res if record["file"] == "lipids.tsv")
        return datetime.datetime.strptime(record["date"], "%B %d %Y")


if __name__ == "__main__":
    SwissLipidGetter.print()
