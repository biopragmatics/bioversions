# -*- coding: utf-8 -*-

"""A getter for KEGG."""

from typing import Mapping

from bioversions.utils import Getter, VersionType, get_soup
import bioregistry

__all__ = [
    "KEGGGetter",
]

URL = "https://www.kegg.jp/kegg/docs/relnote.html"


class KEGGGetter(Getter):
    """A getter for KEGG."""

    name = "KEGG"
    date_fmt = "%B %d, %Y"
    version_type = VersionType.semver_minor
    collection = ["kegg", *bioregistry.get_has_parts("kegg")]

    def get(self) -> Mapping[str, str]:
        """Get the latest KEGG version number."""
        soup = get_soup(URL)
        header = soup.find("h4")
        sibling = header.next_sibling.strip()
        version, date = [part.strip() for part in sibling.split(",", 1)]
        version = version[len("Release ") :]
        return dict(version=version, date=date)


if __name__ == "__main__":
    KEGGGetter.print()
