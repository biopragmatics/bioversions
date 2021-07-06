# -*- coding: utf-8 -*-

"""A getter for PathBank."""

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "PathBankGetter",
]

URL = "https://pathbank.org/"


class PathBankGetter(Getter):
    """A getter for PathBank."""

    bioregistry_id = "pathbank"
    name = "PathBank"
    version_type = VersionType.semver_minor

    def get(self) -> str:
        """Get the latest PathBank version number."""
        soup = get_soup(URL)
        version = (
            soup.find(id="main")
            .find(name="footer")
            .find(**{"class": "wishart-clear"})
            .find(name="strong")
        )
        return version.text


if __name__ == "__main__":
    PathBankGetter.print()
