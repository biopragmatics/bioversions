"""A getter for ChemIDplus."""

import re

from bioversions.utils import Getter, VersionType, requests_get

__all__ = [
    "ChemIDplusGetter",
]

LATEST_URL = "https://ftp.nlm.nih.gov/projects/chemidlease/CurrentChemID.xml"


class ChemIDplusGetter(Getter):
    """A getter for ChemIDplus."""

    bioregistry_id = "chemidplus"
    name = "ChemIDplus"
    date_version_fmt = "%Y-%m-%d"
    homepage_fmt = "https://ftp.nlm.nih.gov/projects/chemidlease/chem.xml.{version}.zip"
    version_type = VersionType.date

    def get(self) -> str:
        """Get the latest ChemIDplus version number."""
        headers = {"Range": "bytes=0-300"}  # leave some slack to capture date
        r = requests_get(LATEST_URL, headers=headers, timeout=30)
        if r.status_code == 206:
            result = re.search(r" date=\"([0-9]{4}-[0-9]{2}-[0-9]{2})\">", r.text)
            if result:
                return result.groups()[0]
        raise ValueError

    @staticmethod
    def homepage_version_transform(version: str) -> str:
        """Replace dots with dashes for ChemIDplus homepage format."""
        return version.replace("-", "")


if __name__ == "__main__":
    ChemIDplusGetter.print()
