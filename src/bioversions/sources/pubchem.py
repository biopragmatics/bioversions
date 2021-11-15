# -*- coding: utf-8 -*-

"""A getter for PubChem."""

import datetime

from bioversions.utils import Getter, VersionType

__all__ = [
    "PubChemGetter",
]


class PubChemGetter(Getter):
    """A getter for PubChem."""

    name = "PubChem"
    homepage_fmt = "https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Monthly/{version}"
    version_type = VersionType.date

    def get(self):
        """Get the latest PubChem version number."""
        return datetime.datetime.now().strftime("%Y-%m-01")


if __name__ == "__main__":
    PubChemGetter.print()
