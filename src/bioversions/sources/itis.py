"""A getter for ITIS."""

from collections.abc import Mapping

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "ITISGetter",
]

URL = "https://itis.gov/downloads/index.html"


class ITISGetter(Getter):
    """A getter for ITIS."""

    bioregistry_id = "itis"
    name = "ITIS"
    date_fmt = "%d-%B-%Y"
    version_type = VersionType.date

    def get(self) -> Mapping[str, str]:
        """Get the latest ITIS version number."""
        soup = get_soup(URL)
        cells = soup.find_all("td")
        for cell in cells:
            if "Database download files are currently from the " not in cell.text:
                continue
            bolds = list(cell.find_all("b"))
            return bolds[1].text
        raise ValueError


if __name__ == "__main__":
    ITISGetter.print()
