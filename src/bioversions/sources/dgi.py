# -*- coding: utf-8 -*-

"""A getter for the `Drug Gene Interaction Database (DGI-DB) <http://www.dgidb.org>`_."""

import os

import bs4
import requests

from bioversions.utils import Getter, VersionType

DOWNLOADS_PAGE = "https://www.dgidb.org/downloads"


class DGIGetter(Getter):
    """A getter for DGI."""

    name = "Drug Gene Interaction Database"
    version_type = VersionType.month
    date_version_fmt = "%Y-%b"

    def get(self):
        """Get the latest DGI version number."""
        res = requests.get(DOWNLOADS_PAGE)
        soup = bs4.BeautifulSoup(res.content, parser="lxml", features="lxml")
        cells = list(soup.select("table#tsv_downloads tbody tr:first-child td:nth-child(2) a"))
        if 1 != len(cells):
            raise ValueError
        cell = cells[0]
        href = cell["href"]
        version = os.path.dirname(os.path.relpath(href, "data/monthly_tsvs"))
        return version


if __name__ == "__main__":
    DGIGetter.print()
