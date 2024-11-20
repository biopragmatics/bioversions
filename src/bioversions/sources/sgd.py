"""A getter for SGD."""

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "SgdGetter",
]

VERSION_FILE = (
    "http://sgd-archive.yeastgenome.org/sequence/S288C_reference/dates_of_genome_releases.tab"
)


class SgdGetter(Getter):
    """A getter for SGD."""

    bioregistry_id = "sgd"
    name = "Saccharomyces Genome Database"
    date_fmt = "%Y-%m-%d"
    version_type = VersionType.date

    def get(self):
        """Get the latest SGD version number."""
        with requests.Session() as session:
            res = session.get(VERSION_FILE)
            d = {}
            lines = list(res.text.splitlines())
            # First 3 lines are headers
            lines = lines[3:]
            for line in lines:
                line = line.strip().split()
                # Some lines contain extra information
                d[line[0]] = line[1].replace("_", "-")
        version = max(d, key=d.get)
        return {
            "version": version,
            "date": d[version],
        }


if __name__ == "__main__":
    SgdGetter.print()
