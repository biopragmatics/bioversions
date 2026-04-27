"""A getter for Pathway Commons."""

from bioversions.utils import Getter, VersionType, find_soup_text, get_soup

__all__ = [
    "PathwayCommonsGetter",
]

URL = "https://www.pathwaycommons.org/"


class PathwayCommonsGetter(Getter):
    """A getter for Pathway Commons."""

    name = "Pathway Commons"
    version_type = VersionType.sequential

    def get(self) -> str:
        """Get the latest Pathway Commons version number."""
        soup = get_soup(URL)
        boost_text = find_soup_text(soup, {"class": "boost"})
        boost_text = boost_text[len("Version ") :]
        boost_text = boost_text.split(":")[0]
        return boost_text


if __name__ == "__main__":
    PathwayCommonsGetter.print()
