# -*- coding: utf-8 -*-

"""A getter for ExPASy."""

import requests
import requests_ftp

from bioversions.utils import Getter

__all__ = [
    'ExPASyGetter',
]

requests_ftp.monkeypatch_session()
URL = 'ftp://ftp.expasy.org/databases/enzyme/enzuser.txt'


class ExPASyGetter(Getter):
    """A getter for ExPASy."""

    name = 'ExPASy'

    def get() -> str:
        """Get the latest ExPASy version number."""
        s = requests.Session()
        s.mount()
        res = s.get(URL, stream=True)
        li = res.iter_lines()
        next(li)
        next(li)
        r = next(li).decode('utf8').strip()[len('Release of '):]
        return r


if __name__ == '__main__':
    ExPASyGetter.print()
