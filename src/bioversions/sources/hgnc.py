# -*- coding: utf-8 -*-

"""A getter for HGNC."""

import datetime

from ..utils import Getter, VersionType, get_soup

__all__ = [
    "HGNCGetter",
]


class HGNCGetter(Getter):
    """A getter for HGNC."""

    bioregistry_id = "hgnc"
    name = "HGNC"
    homepage_fmt = "https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/archive/monthly/json/hgnc_complete_set_{version}.json"

    version_type = VersionType.date

    def get(self) -> str:
        """Get the latest HGNC version number."""
        # TODO scrape https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/archive/monthly/json instead
        return datetime.date.today().strftime("%Y-%m-01")


if __name__ == "__main__":
    HGNCGetter.print()
