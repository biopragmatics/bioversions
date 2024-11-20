"""A getter for SwissLipids."""

import datetime

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "SwissLipidGetter",
]

# View docs at https://www.swisslipids.org/#/api
URL = "https://www.swisslipids.org/api/index.php/downloadData"


class SwissLipidGetter(Getter):
    """A getter for SwissLipids."""

    bioregistry_id = "slm"
    name = "SwissLipids"
    version_type = VersionType.date

    def get(self):
        """Get the latest SwissLipids version number."""
        res = requests.get(URL, timeout=15).json()
        record = next(record for record in res if record["file"] == "lipids.tsv")
        return datetime.datetime.strptime(record["date"], "%B %d %Y")


if __name__ == "__main__":
    SwissLipidGetter.print()
