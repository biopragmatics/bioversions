"""A getter for GTDB."""

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "GTDBGetter",
]

URL = "https://data.ace.uq.edu.au/public/gtdb/data/releases/latest/VERSION.txt"


class GTDBGetter(Getter):
    """A getter for the Genome Taxonomy Database (GTDB)."""

    bioregistry_id = "gtdb"
    name = "Genome Taxonomy Database"
    version_type = VersionType.sequential
    date_fmt = "%b %d, %Y"  # Format to match "Apr 24, 2024"
    homepage_fmt = "https://gtdb.ecogenomic.org/"

    def get(self):
        """Get the latest GTDB version number from VERSION.txt."""
        res = requests.get(URL, timeout=15)
        lines = res.text.strip().split("\n")

        # First line contains version like "v220"
        version_line = next(line for line in lines if line.startswith("v"))
        version = version_line.strip().lstrip("v")

        # Third line contains date like "Released Apr 24, 2024"
        date_line = next(line for line in lines if line.startswith("Released "))
        date = date_line.strip().removeprefix("Released ")

        return {"version": version, "date": date}


if __name__ == "__main__":
    GTDBGetter.print()
