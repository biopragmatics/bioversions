# -*- coding: utf-8 -*-

"""A getter for ZFIN."""

from datetime import datetime

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "ZfinGetter",
]

URL = "https://zfin.org/downloads"


class ZfinGetter(Getter):
    """A getter for ZFIN."""

    bioregistry_id = "zfin"
    name = "Zebrafish Information Network"
    version_type = VersionType.date

    def get(self):
        """Get the latest ZFIN version number."""
        soup = get_soup(URL)
        header = soup.find("h2")
        version = header.text[len("ZFIN Data Reports from: ") :].strip()
        return datetime.strptime(version, "%d %b %Y").strftime("%Y-%m-%d")


if __name__ == "__main__":
    ZfinGetter.print()
