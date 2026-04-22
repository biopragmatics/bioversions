"""A getter for RGD."""

from collections.abc import Iterator

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "RGDGetter",
]

URL = "https://download.rgd.mcw.edu/data_release/GENES_RAT.txt"


class RGDGetter(Getter):
    """A getter for RGD."""

    bioregistry_id = "rgd"
    name = "Rat Genome Database"
    date_fmt = "%Y-%m-%d"
    version_type = VersionType.date

    def get(self) -> str:
        """Get the latest RGD version number."""
        with requests.Session() as session:
            res = session.get(URL, stream=True)
            lines: Iterator[str] = res.iter_lines(decode_unicode=True)
            next(lines)
            next(lines)
            date = next(lines).split(" ")[2].replace("/", "-")
        return date


if __name__ == "__main__":
    RGDGetter.print()
