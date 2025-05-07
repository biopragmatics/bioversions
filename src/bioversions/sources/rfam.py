"""A getter for Rfam."""

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "RfamGetter",
]


class RfamGetter(Getter):
    """A getter for Rfam."""

    bioregistry_id = "rfam"
    name = "Rfam"
    homepage_fmt = "https://ftp.ebi.ac.uk/pub/databases/Rfam/{version}/"
    version_type = VersionType.semver_minor

    def get(self) -> str:
        """Get the latest Rfam version number."""
        res = requests.get("https://ftp.ebi.ac.uk/pub/databases/Rfam/CURRENT/README", timeout=15)
        for line in res.iter_lines():
            line = line.decode("utf8").strip()
            if line.startswith("Release "):
                return line[len("Release ") :]
        raise ValueError


if __name__ == "__main__":
    RfamGetter.print()
