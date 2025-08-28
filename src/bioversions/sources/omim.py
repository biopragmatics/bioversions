"""A getter for the OMIM."""

import datetime
from typing import ClassVar

from dateutil.parser import parse

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "OMIMGetter",
]


class OMIMGetter(Getter):
    """A getter for OMIM."""

    name = "Online Mendelian Inheritance in Man"
    version_type = VersionType.date
    collection: ClassVar[list[str]] = ["omim.ps", "omim"]

    def get(self) -> datetime.datetime:
        """Get the latest OMIM version number."""
        soup = get_soup("https://omim.org/")
        for tag in soup.find_all("h5"):
            text = tag.text.strip()
            if text.startswith("Updated"):
                rv = text[len("Updated") :].strip()
                return parse(rv)
        raise ValueError


if __name__ == "__main__":
    OMIMGetter.print()
