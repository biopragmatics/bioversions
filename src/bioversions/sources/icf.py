"""A getter for ICF."""

import warnings

import requests
from urllib3.exceptions import InsecureRequestWarning

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
        with warnings.catch_warnings():
            warnings.simplefilter(action="ignore", category=InsecureRequestWarning)
            response = requests.get(URL, allow_redirects=True, timeout=15, verify=False)  # noqa:S501
        final_url = response.url
        return final_url[len("https://icd.who.int/browse/") :].split("/")[0]


if __name__ == "__main__":
    ICFGetter.print()
