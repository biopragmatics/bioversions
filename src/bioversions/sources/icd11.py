"""A getter for ICD11."""

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "ICD11Getter",
]

URL = "https://icd.who.int/browse/latest-release/mms/en"


class ICD11Getter(Getter):
    """A getter for ICD11."""

    bioregistry_id = "icd11"
    name = "International Classification of Diseases, 11th Revision"
    version_type = VersionType.date
    date_version_fmt = "%Y-%m"

    def get(self) -> str:
        """Get the latest ICD11 version number."""
        response = requests.get(URL, allow_redirects=True, timeout=15)
        final_url = response.url
        return final_url[len("https://icd.who.int/browse/") :].split("/")[0]


if __name__ == "__main__":
    ICD11Getter.print()
