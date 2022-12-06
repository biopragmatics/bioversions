# -*- coding: utf-8 -*-

"""A getter for DrugBank."""

from operator import itemgetter

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "DrugBankGetter",
]

URL = "https://go.drugbank.com/releases.json"


class DrugBankGetter(Getter):
    """A getter for DrugBank."""

    bioregistry_id = "drugbank"
    name = "DrugBank"
    homepage_fmt = "https://go.drugbank.com/releases/{version}"
    date_fmt = "%Y-%m-%d"
    version_type = VersionType.semver

    def get(self):
        """Get the latest DrugBank version number."""
        res = requests.get(URL)
        res.raise_for_status()
        latest = max(res.json(), key=itemgetter("released_on"))
        return dict(date=latest["released_on"], version=latest["version"])

    @staticmethod
    def homepage_version_transform(version: str) -> str:
        """Replace dots with dashes for DrugBank homepage format."""
        return version.replace(".", "-")


if __name__ == "__main__":
    DrugBankGetter.print()
