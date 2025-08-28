"""A getter for SPDX."""

from typing import ClassVar

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "SPDXGetter",
]

DATA_URL = "https://github.com/spdx/license-list-data/raw/refs/heads/main/json/licenses.json"


class SPDXGetter(Getter):
    """A getter for SPDX."""

    bioregistry_id = "spdx"
    name = "Software Package Data Exchange License"
    version_type = VersionType.other
    collection: ClassVar[list[str]] = ["spdx", "spdx.term"]

    def get(self) -> str:
        """Get the latest SwissLipids version number."""
        return requests.get(DATA_URL, timeout=5).json()["licenseListVersion"]


if __name__ == "__main__":
    SPDXGetter.print()
