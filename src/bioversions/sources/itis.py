"""A getter for ITIS."""

import datetime

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "ITISGetter",
]

URL = "https://www.itis.gov/DisplayPresentDate"


class ITISGetter(Getter):
    """A getter for ITIS."""

    bioregistry_id = "itis"
    name = "ITIS"
    version_type = VersionType.date

    def get(self) -> datetime.datetime:
        """Get the latest ITIS version number."""
        res = requests.get(URL, timeout=3).text
        return datetime.datetime.strptime(res, "%d-%b-%Y")


if __name__ == "__main__":
    ITISGetter.print()
