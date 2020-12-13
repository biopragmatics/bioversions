# -*- coding: utf-8 -*-

"""A getter for WikiPathways."""

import ftplib

from bioversions.utils import Getter

__all__ = [
    'MirbaseGetter',
]

PREFIX = '0_THIS_IS_RELEASE_'


class MirbaseGetter(Getter):
    """A getter for miRBase."""

    name = 'miRBase'
    homepage_fmt = 'ftp://mirbase.org/pub/mirbase/{version}/'

    def get(self):
        """Get the latest Mirbase version number."""
        with ftplib.FTP('mirbase.org') as ftp:
            ftp.login()
            ftp.cwd('pub/mirbase/CURRENT')
            for name, _ in ftp.mlsd():
                if name.startswith(PREFIX):
                    return name.removeprefix(PREFIX)
        raise ValueError


if __name__ == '__main__':
    MirbaseGetter.print()
