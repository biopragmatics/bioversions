# -*- coding: utf-8 -*-

"""A getter for the Antibody Registry."""

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "AntibodyRegistryGetter",
]


class AntibodyRegistryGetter(Getter):
    """A getter for the Antibody Registry."""

    bioregistry_id = "antibodyregistry"
    name = "Antibody Registry"
    homepage_fmt = "https://antibodyregistry.org/"
    version_type = VersionType.semver_minor

    def get(self):
        """Get the latest Antibody Registry version number."""
        soup = get_soup("https://antibodyregistry.org/")
        return soup.find(**{"class": "footer"}).find("a").text.lstrip("v")


if __name__ == "__main__":
    AntibodyRegistryGetter.print()
