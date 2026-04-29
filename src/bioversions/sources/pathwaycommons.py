"""A getter for Pathway Commons."""

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "PathwayCommonsGetter",
]

URL = "https://download.baderlab.org/PathwayCommons/PC2/"


class PathwayCommonsGetter(Getter):
    """A getter for Pathway Commons."""

    name = "Pathway Commons"
    version_type = VersionType.sequential

    def get(self) -> str:
        """Get the latest Pathway Commons version number."""
        soup = get_soup(URL)
        hrefs = {
            int(anchor.attrs["href"].lstrip("v").rstrip("/"))
            for anchor in soup.find_all("a")
            if anchor.attrs is not None
            and "href" in anchor.attrs
            and isinstance(anchor.attrs["href"], str)
            and anchor.attrs["href"].startswith("v")
        }
        return str(max(hrefs))


if __name__ == "__main__":
    PathwayCommonsGetter.print()
