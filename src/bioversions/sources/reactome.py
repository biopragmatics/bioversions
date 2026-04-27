"""A getter for Reactome."""

from ..utils import Getter, VersionType, find_soup_tag, find_soup_text, get_soup

__all__ = [
    "ReactomeGetter",
]

URL = "https://reactome.org/"


class ReactomeGetter(Getter):
    """A getter for Reactome."""

    bioregistry_id = "reactome"
    name = "Reactome"
    version_type = VersionType.sequential

    def get(self) -> str:
        """Get the latest BioGRID version number."""
        soup = get_soup(URL)
        manifest = find_soup_tag(soup, id="fav-portfoliowrap")
        header = find_soup_text(manifest, "h3")
        return header.split()[1]


if __name__ == "__main__":
    ReactomeGetter.print()
