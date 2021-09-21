# -*- coding: utf-8 -*-

"""A getter for HPRD."""

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "HPRDGetter",
]

URL = "https://hprd.org/download"


class HPRDGetter(Getter):
    """A getter for HPRD."""

    bioregistry_id = "hprd"
    name = "Human Protein Reference Databas"
    date_fmt = "%Y-%m-%d"
    version_type = VersionType.sequential

    def get(self):
        """Get the latest DrugBank version number."""
        soup = get_soup(URL)
        rows = soup.find("form", {"name": "form1"}).find("table").find("table").find_all("tr")
        row = next(list(rows)[3])
        print(row)

if __name__ == "__main__":
    HPRDGetter.print()
