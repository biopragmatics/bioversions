# -*- coding: utf-8 -*-

"""A getter for Reactome."""

from ..utils import Getter, VersionType, get_soup

__all__ = [
    "ReactomeGetter",
]

URL = "https://reactome.org/"


class ReactomeGetter(Getter):
    """A getter for Reactome."""

    bioregistry_id = "reactome"
    name = "Reactome"
    version_type = VersionType.sequential

    def get(self):
        """Get the latest BioGRID version number."""
        soup = get_soup(URL)
        manifest = soup.find(id="fav-portfoliowrap")
        header = manifest.find("h3")
        return header.text.split()[1]


if __name__ == "__main__":
    ReactomeGetter.print()
