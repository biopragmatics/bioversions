"""A getter for ICD10."""

import warnings

import requests
from urllib3.exceptions import InsecureRequestWarning

from bioversions.utils import Getter, VersionType

__all__ = [
    "ICD10Getter",
]

URL = "https://icd.who.int/browse10/"


class ICD10Getter(Getter):
    """A getter for ICD10."""

    bioregistry_id = "icd10"
    name = "International Classification of Diseases, 10th Revision"
    version_type = VersionType.date
    date_version_fmt = "%Y"

    def get(self) -> str:
        """Get the latest ICD10 version number."""
        with warnings.catch_warnings():
            warnings.simplefilter(action="ignore", category=InsecureRequestWarning)
            response = requests.get(URL, allow_redirects=True, timeout=15, verify=False)  # noqa:S501
        final_url = response.url
        return final_url[len("https://icd.who.int/browse10/") :].split("/")[0]


if __name__ == "__main__":
    ICD10Getter.print()
