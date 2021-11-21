# -*- coding: utf-8 -*-

"""A getter for UMLS."""

from datetime import datetime

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "UMLSGetter",
]

URL = "https://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html"


class UMLSGetter(Getter):
    """A getter for UMLS."""

    bioregistry_id = "umls"
    name = "UMLS"
    version_type = VersionType.other

    def get(self) -> datetime:
        """Get the latest UMLS version number."""
        soup = get_soup(URL)
        raw_version = soup.find("div", {"id": "body"}).find("h2")
        return raw_version.text.split()[0]


if __name__ == "__main__":
    UMLSGetter.print()
