# -*- coding: utf-8 -*-

"""A getter for HGNC."""

import logging

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "HGNCGetter",
]

logger = logging.getLogger(__name__)

PATH = "https://ftp.ebi.ac.uk/pub/databases/genenames/new/archive/monthly/json/"
PREFIX = "hgnc_complete_set_"
SUFFIX = ".json"


class HGNCGetter(Getter):
    """A getter for HGNC."""

    bioregistry_id = "hgnc"
    name = "HGNC"
    homepage_fmt = (
        "http://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/"
        "archive/monthly/json/hgnc_complete_set_{version}.json"
    )

    version_type = VersionType.date

    def get(self) -> str:
        """Get the latest HGNC version number."""
        soup = get_soup(PATH)
        return max(
            anchor.attrs["href"][len(PREFIX) : -len(SUFFIX)]
            for anchor in soup.find_all("a")
            if anchor.attrs["href"].startswith(PREFIX)
        )


if __name__ == "__main__":
    HGNCGetter.print()
