# -*- coding: utf-8 -*-

"""A getter for DrugBank."""

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "DrugBankGetter",
]

URL = "https://go.drugbank.com/releases/latest"


class DrugBankGetter(Getter):
    """A getter for DrugBank."""

    bioregistry_id = "drugbank"
    name = "DrugBank"
    homepage_fmt = "https://go.drugbank.com/releases/{version}"
    date_fmt = "%Y-%m-%d"
    version_type = VersionType.semver

    def get(self):
        """Get the latest DrugBank version number."""
        soup = get_soup(URL)
        manifest = soup.find(**{"class": "download-table"}).find("table").find("tbody").find("tr")
        manifest = list(manifest)
        date = manifest[1].text
        version = manifest[2].text
        return dict(date=date, version=version)

    @staticmethod
    def homepage_version_transform(version: str) -> str:
        """Replace dots with dashes for DrugBank homepage format."""
        return version.replace(".", "-")


if __name__ == "__main__":
    DrugBankGetter.print()
