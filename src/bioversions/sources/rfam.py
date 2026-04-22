"""A getter for Rfam."""

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "RfamGetter",
]
URL = "https://ftp.ebi.ac.uk/pub/databases/Rfam/CURRENT/README"


class RfamGetter(Getter):
    """A getter for Rfam."""

    bioregistry_id = "rfam"
    name = "Rfam"
    homepage_fmt = "https://ftp.ebi.ac.uk/pub/databases/Rfam/{version}/"
    version_type = VersionType.semver_minor

    def get(self) -> str:
        """Get the latest Rfam version number."""
        res = requests.get(URL, timeout=15)
        res.raise_for_status()
        for line_bytes in res.iter_lines():
            line: str = line_bytes.decode("utf-8").strip()
            if line.startswith("Release "):
                return line[len("Release ") :]
        raise ValueError


if __name__ == "__main__":
    RfamGetter.print()
