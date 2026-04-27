"""A getter for BiGG."""

from datetime import datetime

from bioversions.utils import Getter, ReleaseDict, VersionType, requests_get

__all__ = [
    "BiGGGetter",
]

URL = "http://bigg.ucsd.edu/api/v2/database_version"


class BiGGGetter(Getter):
    """A getter for BiGG."""

    name = "BiGG"
    version_type = VersionType.semver

    def get(self) -> ReleaseDict:
        """Get the latest BiGG version number."""
        res = requests_get(URL, timeout=15).json()
        date = datetime.fromisoformat(res["last_updated"])
        return {
            "version": res["bigg_models_version"],
            "date": date,
        }


if __name__ == "__main__":
    BiGGGetter.print()
