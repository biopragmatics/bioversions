"""A getter for DepMap."""

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "DepMapGetter",
]

URL = "https://depmap.org/portal/download/api/downloads"


class DepMapGetter(Getter):
    """A getter for DepMap."""

    name = "DepMap"
    version_type = VersionType.other

    def get(self) -> str:
        """Get the latest DepMap version number."""
        res = requests.get(URL, timeout=15)
        latest = next(release for release in res.json()["releaseData"] if release["isLatest"])
        return latest["releaseName"][len("DepMap Public ") :]


if __name__ == "__main__":
    DepMapGetter.print()
