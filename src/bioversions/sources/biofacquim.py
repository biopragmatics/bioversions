# -*- coding: utf-8 -*-

"""A getter for Biofacquim."""

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "BiofacquimGetter",
]


class BiofacquimGetter(Getter):
    """A getter for Biofacquim."""

    name = "Biofacquim"
    version_type = VersionType.semver_minor

    def get(self) -> str:
        """Get the latest NPASS version number."""
        soup = get_soup("https://biofacquim.herokuapp.com/")
        h3 = soup.find(name="h3")
        return h3.text[len("version ") :]


if __name__ == "__main__":
    BiofacquimGetter.print()
