# -*- coding: utf-8 -*-

"""A getter for Ensembl."""

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "EnsemblGetter",
]

URL = "https://useast.ensembl.org/index.html"


class EnsemblGetter(Getter):
    """A getter for Ensembl."""

    bioregistry_id = "ensembl"
    name = "Ensembl"
    homepage_fmt = "https://www.ensembl.org"
    date_fmt = "%B %Y"
    version_type = VersionType.sequential

    def get(self):
        """Get the latest Ensembl version number."""
        soup = get_soup(URL)
        manifest = soup.find(**{"class": "box-header"}).text
        version, date = manifest.rstrip(")").split("(", 1)
        return dict(version=version.split()[-1], date=date)


if __name__ == "__main__":
    EnsemblGetter.print()
