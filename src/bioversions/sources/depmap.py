"""A getter for DepMap."""

from typing import cast

import requests

from bioversions.utils import Getter, VersionType
from bioversions.version import get_version

__all__ = [
    "DepMapGetter",
]

URL = "https://depmap.org/portal/download/api/downloads"


class DepMapGetter(Getter):
    """A getter for DepMap."""

    name = "DepMap"
    version_type = VersionType.other
    bioregistry_id = "depmap"

    def get(self) -> str:
        """Get the latest DepMap version number."""
        res = requests.get(
            URL,
            timeout=15,
            headers={"User-Agent": f"bioversions v{get_version(with_git_hash=True)}"},
        )
        res_json = res.json()
        latest = next(release for release in res_json["releaseData"] if release["isLatest"])
        rv = cast(str, latest["releaseName"][len("DepMap Public ") :])
        return rv


if __name__ == "__main__":
    DepMapGetter.print()
