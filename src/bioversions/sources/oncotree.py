# -*- coding: utf-8 -*-

"""A getter for OncoTree."""

from ..utils import Getter, VersionType
import requests

__all__ = [
    "OncoTreeGetter",
]

URL = "http://oncotree.mskcc.org/api/versions"


class OncoTreeGetter(Getter):
    """A getter for OncoTree."""

    bioregistry_id = "oncotree"
    name = "OncoTree"
    version_type = VersionType.date
    date_version_fmt = "%Y-%m-%d"

    def get(self) -> str:
        """Get the latest OncoTree version number."""
        res = requests.get(URL, params={"format": "json"})
        res_json = res.json()
        version = next(
            (r["release_date"] for r in res_json if r["api_identifier"] == "oncotree_latest_stable")
        )
        return version


if __name__ == "__main__":
    OncoTreeGetter.print()
