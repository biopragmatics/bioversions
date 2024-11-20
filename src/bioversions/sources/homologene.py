"""A getter for HomoloGene."""

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "HomoloGeneGetter",
]

URL = "https://ftp.ncbi.nih.gov/pub/HomoloGene/current/RELEASE_NUMBER"


class HomoloGeneGetter(Getter):
    """A getter for HomoloGene."""

    bioregistry_id = "homologene"
    name = "HomoloGene"
    version_type = VersionType.sequential

    def get(self) -> str:
        """Get the latest HomoloGene version number."""
        s = requests.Session()
        res = s.get(URL, stream=True)
        return res.text.strip()


if __name__ == "__main__":
    HomoloGeneGetter.print()
