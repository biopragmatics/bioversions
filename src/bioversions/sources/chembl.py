# -*- coding: utf-8 -*-

"""A getter for ChEMBL."""

import ftplib
import io

from bioversions.utils import Getter, VersionType

__all__ = [
    "ChEMBLGetter",
]

RELEASE_PREFIX = "* Release:"
DATE_PREFIX = "* Date:"


class ChEMBLGetter(Getter):
    """A getter for ChEMBL."""

    bioregistry_id = "chembl"
    name = "ChEMBL"
    homepage_fmt = "ftp://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_{version}"
    date_fmt = "%d/%m/%Y"
    version_type = VersionType.sequential

    def get(self):
        """Get the latest ChEMBL version number."""
        bio = io.BytesIO()
        with ftplib.FTP("ftp.ebi.ac.uk") as ftp:
            ftp.login()
            ftp.retrbinary("RETR pub/databases/chembl/ChEMBLdb/latest/README", bio.write)
        bio.seek(0)
        version, date = None, None
        for line in bio.read().decode("utf-8").split("\n"):
            if line.startswith(RELEASE_PREFIX):
                version = _removeprefix(_removeprefix(line, RELEASE_PREFIX).strip(), "chembl_")
            elif line.startswith(DATE_PREFIX):
                date = _removeprefix(line, DATE_PREFIX).strip()
        if version is None or date is None:
            raise ValueError
        return dict(date=date, version=version)


def _removeprefix(s, prefix):
    if s.startswith(prefix):
        return s[len(prefix) :]
    return s


if __name__ == "__main__":
    ChEMBLGetter.print()
