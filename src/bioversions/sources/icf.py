# -*- coding: utf-8 -*-

"""A getter for ICF."""

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "ICFGetter",
]

URL = "https://icd.who.int/browse/latest-release/icf/en"


class ICFGetter(Getter):
    """A getter for ICF."""

    bioregistry_id = "icf"
    name = "International Classification of Functioning, Disability and Health"
    version_type = VersionType.date
    date_version_fmt = "%Y-%m"

    def get(self) -> str:
        """Get the latest ICF version number."""
        response = requests.get(URL, allow_redirects=True)
        final_url = response.url
        return final_url[len("https://icd.who.int/browse/") :].split("/")[0]


if __name__ == "__main__":
    ICFGetter.print()
