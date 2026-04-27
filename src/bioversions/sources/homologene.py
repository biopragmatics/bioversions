"""A getter for HomoloGene."""

from bioversions.utils import Getter, VersionType, requests_get

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
        res = requests_get(URL, timeout=15)
        return res.text.strip()


if __name__ == "__main__":
    HomoloGeneGetter.print()
