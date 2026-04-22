"""A getter for ZFIN."""

import datetime

from bioversions.utils import Getter, VersionType, find_text, get_soup

__all__ = [
    "ZfinGetter",
]

URL = "https://zfin.org/downloads"


class ZfinGetter(Getter):
    """A getter for ZFIN."""

    bioregistry_id = "zfin"
    name = "Zebrafish Information Network"
    version_type = VersionType.date

    def get(self) -> datetime.date:
        """Get the latest ZFIN version number."""
        soup = get_soup(URL)
        header_text = find_text(soup, "h2")
        version = header_text[len("ZFIN Data Reports from: ") :].strip()
        return datetime.date.strptime(version, "%d %b %Y")


if __name__ == "__main__":
    ZfinGetter.print()
