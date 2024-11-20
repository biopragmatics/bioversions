"""A getter for the OMIM."""

from typing import ClassVar

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "OMIMGetter",
]


class OMIMGetter(Getter):
    """A getter for OMIM."""

    name = "Online Mendelian Inheritance in Man"
    date_version_fmt = "%B %d, %Y"
    version_type = VersionType.date
    collection: ClassVar[list[str]] = ["omim.ps", "omim"]

    def get(self) -> str:
        """Get the latest OMIM version number."""
        soup = get_soup("https://omim.org/")
        for tag in soup.find_all("h5"):
            text = tag.text.strip()
            if text.startswith("Updated"):
                rv = text[len("Updated") :].strip()
                rv = rv.replace("nd", "").replace("st", "").replace("rd", "").replace("th", "")
                return rv
        raise ValueError


if __name__ == "__main__":
    OMIMGetter.print()
