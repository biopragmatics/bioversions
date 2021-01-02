# -*- coding: utf-8 -*-

"""A getter for ExPASy."""

import requests

from bioversions.utils import Getter

__all__ = [
    'ExPASyGetter',
]

URL = 'ftp://ftp.expasy.org/databases/enzyme/enzuser.txt'


class ExPASyGetter(Getter):
    """A getter for ExPASy."""

    name = 'ExPASy'
    date_version_fmt = '%d-%b-%Y'

    def get(self) -> str:
        """Get the latest ExPASy version number."""
        s = requests.Session()
        res = s.get(URL, stream=True)
        li = res.iter_lines()
        next(li)
        next(li)
        r = next(li).decode('utf8').strip()[len('Release of '):]
        return r


if __name__ == '__main__':
    ExPASyGetter.print()
