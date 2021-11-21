# -*- coding: utf-8 -*-

"""A getter for DrugCentral."""

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "DrugCentralGetter",
]

URL = "https://drugcentral.org/download"


class DrugCentralGetter(Getter):
    """A getter for DrugCentral."""

    bioregistry_id = "drugcentral"
    name = "DrugCentral"
    date_version_fmt = "%Y_%m_%d"
    homepage_fmt = href = "https://unmtid-shinyapps.net/download/DrugCentral/{version}"
    version_type = VersionType.date

    def get(self) -> str:
        """Get the latest DrugCentral version number."""
        soup = get_soup(URL)
        manifest = soup.find("h4", **{"class": "txt-sec"}).find("a")
        return manifest.attrs["href"].split("/")[-2]


if __name__ == "__main__":
    DrugCentralGetter.print()
