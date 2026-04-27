"""A getter for DepMap."""

from typing import cast

from bioversions.utils import Getter, VersionType, requests_get

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
        res = requests_get(URL, timeout=15)
        res_json = res.json()
        latest = next(release for release in res_json["releaseData"] if release["isLatest"])
        rv = cast(str, latest["releaseName"][len("DepMap Public ") :])
        return rv


if __name__ == "__main__":
    DepMapGetter.print()
