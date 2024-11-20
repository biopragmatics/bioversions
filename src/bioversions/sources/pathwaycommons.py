"""A getter for Pathway Commons."""

from bioversions.utils import Getter, VersionType, get_soup

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
        boost = soup.find(**{"class": "boost"})
        boost = boost.text[len("Version ") :]
        boost = boost.split(":")[0]
        return boost


if __name__ == "__main__":
    PathwayCommonsGetter.print()
