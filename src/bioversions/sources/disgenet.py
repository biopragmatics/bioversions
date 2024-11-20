"""A getter for DisGeNet."""

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "DisGeNetGetter",
]

URL = "https://www.disgenet.org/api/version/"


class DisGeNetGetter(Getter):
    """A getter for DisGeNet."""

    name = "DisGeNet"
    date_fmt = "%B %Y"
    version_type = VersionType.sequential

    def get(self):
        """Get the latest DisGeNet version number."""
        res = requests.get(URL, params={"format": "json"}, timeout=15)
        res_json = res.json()
        version = res_json["database_version"].split()[-1].lstrip("v")
        return {
            "version": version,
            "date": res_json["lastUpdate"],
        }


if __name__ == "__main__":
    DisGeNetGetter.print()
