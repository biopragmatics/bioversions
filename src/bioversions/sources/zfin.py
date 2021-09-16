# -*- coding: utf-8 -*-

"""A getter for ZFIN."""

from typing import Mapping

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "ZfinGetter",
]

URL = "https://zfin.org/downloads"


class ZfinGetter(Getter):
    """A getter for ZFIN."""

    bioregistry_id = "zfin"
    name = "Zebrafish Information Network"
    date_version_fmt = "%d %b %Y"
    version_type = VersionType.date

    def get(self) -> Mapping[str, str]:
        """Get the latest ZFIN version number."""
        soup = get_soup(URL)
        header = soup.find("h2")
        version = header.text[len("ZFIN Data Reports from: ") :].strip()
        return version


if __name__ == "__main__":
    ZfinGetter.print()
