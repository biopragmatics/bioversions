"""A getter for `SIGNOR <https://signor.uniroma2.it>`_."""

import datetime
from typing import ClassVar

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "SignorGetter",
]

URL = "https://signor.uniroma2.it/downloads.php"
TEXT = "Click here to download the latest stable release"


class SignorGetter(Getter):
    """A getter for SIGNOR."""

    name = "SIGNOR"
    version_type = VersionType.date
    date_fmt = "%B %Y"
    collection: ClassVar[list[str]] = ["signor", "signor.relation"]

    def get(self) -> datetime.datetime:
        """Get the latest SIGNOR version number."""
        soup = get_soup(URL)
        for p in soup.find_all("p"):
            if TEXT in p.text:
                _, _, after = p.text.partition(TEXT)
                after = after.strip().lstrip("(").rstrip(")")
                return datetime.datetime.strptime(after, "%B %Y")
        raise RuntimeError


if __name__ == "__main__":
    SignorGetter.print()
