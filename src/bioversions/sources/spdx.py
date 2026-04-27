"""A getter for SPDX."""

from typing import ClassVar

from bioversions.utils import Getter, VersionType, requests_get

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
        res = requests_get(DATA_URL, timeout=5)
        res_json: dict[str, str] = res.json()
        return res_json["licenseListVersion"]


if __name__ == "__main__":
    SPDXGetter.print()
