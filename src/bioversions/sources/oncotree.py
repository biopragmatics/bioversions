"""A getter for OncoTree."""

import requests

from ..utils import Getter, VersionType

__all__ = [
    "OncoTreeGetter",
]


class OncoTreeGetter(Getter):
    """A getter for OncoTree."""

    bioregistry_id = "oncotree"
    name = "OncoTree"
    homepage_fmt = "http://oncotree.mskcc.org/api/tumorTypes?version=oncotree_{version}"
    version_type = VersionType.date
    date_version_fmt = "%Y-%m-%d"

    def get(self) -> str:
        """Get the latest OncoTree version number."""
        res = requests.get(
            "http://oncotree.mskcc.org/api/versions", params={"format": "json"}, timeout=5
        )
        res_json = res.json()
        version = next(
            r["release_date"] for r in res_json if r["api_identifier"] == "oncotree_latest_stable"
        )
        return version

    @staticmethod
    def homepage_version_transform(version: str) -> str:
        """Reformat version value for OncoTree data URL."""
        return version.replace("-", "_")


if __name__ == "__main__":
    OncoTreeGetter.print()
