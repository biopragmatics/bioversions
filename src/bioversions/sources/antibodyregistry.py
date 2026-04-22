"""A getter for the Antibody Registry."""

from typing import cast

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "AntibodyRegistryGetter",
]

URL = "https://www.antibodyregistry.org/api/datainfo"


class AntibodyRegistryGetter(Getter):
    """A getter for the Antibody Registry."""

    bioregistry_id = "antibodyregistry"
    name = "Antibody Registry"
    homepage_fmt = "https://antibodyregistry.org/"
    version_type = VersionType.date

    def get(self) -> str:
        """Get the latest Antibody Registry version number."""
        res = requests.get(URL, timeout=3)
        res_json = res.json()
        return cast(str, res_json["lastupdate"])


if __name__ == "__main__":
    AntibodyRegistryGetter.print()
