"""A getter for KEGG."""

from collections.abc import Mapping
from typing import ClassVar

import bioregistry

from bioversions.utils import Getter, VersionType, find, get_soup

__all__ = [
    "KEGGGetter",
]

URL = "https://www.kegg.jp/kegg/docs/relnote.html"


class KEGGGetter(Getter):
    """A getter for KEGG."""

    name = "KEGG"
    date_fmt = "%B %d, %Y"
    version_type = VersionType.semver_minor
    collection: ClassVar[list[str]] = ["kegg", *(bioregistry.get_has_parts("kegg") or [])]

    def get(self) -> Mapping[str, str]:
        """Get the latest KEGG version number."""
        soup = get_soup(URL)
        header = find(soup, "h4")
        sibling = header.next_sibling
        if not sibling:
            raise ValueError
        sibling_text = sibling.text.strip()
        version, date = (part.strip() for part in sibling_text.split(",", 1))
        version = version[len("Release ") :]
        return {"version": version, "date": date}


if __name__ == "__main__":
    KEGGGetter.print()
