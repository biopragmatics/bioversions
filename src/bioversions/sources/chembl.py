# -*- coding: utf-8 -*-

"""A getter for ChEBML."""

import ftplib
import io

from bioversions.utils import Getter

__all__ = [
    'ChEBMLGetter',
]

RELEASE_PREFIX = '* Release:'
DATE_PREFIX = '* Date:'


class ChEBMLGetter(Getter):
    """A getter for ChEBML."""

    name = 'ChEBML'
    homepage_fmt = 'ftp://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_{version}'

    def get(self):
        """Get the latest ChEBML version number."""
        bio = io.BytesIO()
        with ftplib.FTP('ftp.ebi.ac.uk') as ftp:
            ftp.login()
            ftp.retrbinary('RETR pub/databases/chembl/ChEMBLdb/latest/README', bio.write)
        bio.seek(0)
        version, date = None, None
        for line in bio.read().decode('utf-8').split('\n'):
            if line.startswith(RELEASE_PREFIX):
                version = line.removeprefix(RELEASE_PREFIX).strip().removeprefix('chembl_')
            elif line.startswith(DATE_PREFIX):
                date = line.removeprefix(DATE_PREFIX).strip()
        if version is None or date is None:
            raise ValueError
        return dict(date=date, version=version)


if __name__ == '__main__':
    ChEBMLGetter.print()
