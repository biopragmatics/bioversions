# -*- coding: utf-8 -*-

"""A getter for the NCI Thesaurus."""

from ..utils import Getter, VersionType, get_soup

__all__ = [
    "NCItGetter",
]

URL = "https://ncithesaurus.nci.nih.gov/ncitbrowser/"


class NCItGetter(Getter):
    """A getter for the NCI Thesaurus."""

    bioregistry_id = "ncit"
    name = "National Cancer Institute Thesaurus"
    version_type = VersionType.other

    def get(self) -> str:
        """Get the latest NCIt version number."""
        soup = get_soup(URL)
        version = soup.find("input", {"id": "version"}).attrs["value"]
        return version


if __name__ == "__main__":
    NCItGetter.print()
