# -*- coding: utf-8 -*-

"""A getter for InterPro."""

from bioversions.utils import Getter, _get_ftp_version

__all__ = [
    'InterProGetter',
]


class InterProGetter(Getter):
    """A getter for InterPro."""

    name = 'InterPro'
    homepage_fmt = 'ftp://ftp.ebi.ac.uk/pub/databases/interpro/{version}/'

    def get(self):
        """Get the latest InterPro version number."""
        return _get_ftp_version('ftp.ebi.ac.uk', 'pub/databases/interpro/')


if __name__ == '__main__':
    InterProGetter.print()
