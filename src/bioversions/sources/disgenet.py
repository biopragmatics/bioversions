"""A getter for DisGeNet."""

from bioversions.utils import Getter, VersionType, requests_get

__all__ = [
    "DisGeNetGetter",
]

URL = "https://ca346j0lmg.execute-api.eu-central-1.amazonaws.com/releases"


class DisGeNetGetter(Getter):
    """A getter for DisGeNet."""

    name = "DisGeNet"
    version_type = VersionType.sequential

    def get(self) -> str:
        """Get the latest DisGeNet version number."""
        res = requests_get(URL, timeout=15)
        res_json = res.json()
        version: str = res_json["releases"][0]["version"]
        return version.lstrip("v")


if __name__ == "__main__":
    DisGeNetGetter.print()
