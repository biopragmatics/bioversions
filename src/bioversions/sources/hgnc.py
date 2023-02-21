# -*- coding: utf-8 -*-

"""A getter for HGNC."""

import ftplib

from ..utils import Getter, VersionType

__all__ = [
    "HGNCGetter",
]

HOST = "ftp.ebi.ac.uk"
PATH = "pub/databases/genenames/hgnc/archive/monthly/json/"
PREFIX = "hgnc_complete_set_"
SUFFIX = ".json"


class HGNCGetter(Getter):
    """A getter for HGNC."""

    bioregistry_id = "hgnc"
    name = "HGNC"
    homepage_fmt = (
        "https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/"
        "archive/monthly/json/hgnc_complete_set_{version}.json"
    )

    version_type = VersionType.date

    def get(self) -> str:
        """Get the latest HGNC version number."""
        with ftplib.FTP(HOST) as ftp:
            ftp.login()
            ftp.cwd(PATH)
            version = max(
                name[len(PREFIX) : -len(SUFFIX)] for name in ftp.nlst() if name.startswith(PREFIX)
            )
        return version


if __name__ == "__main__":
    HGNCGetter.print()
