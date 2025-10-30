"""A getter for ChEBI."""

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "ChEBIGetter",
]

README = "https://ftp.ebi.ac.uk/pub/databases/chebi/ontology/README"
VERSION_PREFIX = "* ChEBI Release:"
DATE_PREFIX = "* Date of last update:"


class ChEBIGetter(Getter):
    """A getter for ChEBI."""

    bioregistry_id = "chebi"
    name = "ChEBI"
    version_type = VersionType.sequential
    date_fmt = "%Y-%m-%d"

    def get(self):
        """Get the latest ChEBI version number."""
        res = requests.get(README, timeout=5)
        res.raise_for_status()

        rv = {}
        for line in res.iter_lines():
            line = line.decode()
            if line.startswith(VERSION_PREFIX):
                rv["version"] = line.removeprefix(VERSION_PREFIX).strip()
            elif line.startswith(DATE_PREFIX):
                rv["date"] = line.removeprefix(DATE_PREFIX).strip()

        if not rv:
            raise ValueError(f"was not able to parse ChEBI version from {README}")

        return rv


if __name__ == "__main__":
    ChEBIGetter.print()
