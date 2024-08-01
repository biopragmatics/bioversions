# -*- coding: utf-8 -*-

"""A getter for the `Drug Gene Interaction Database (DGI-DB) <http://www.dgidb.org>`_."""

import os

import bs4
import requests

from bioversions.utils import Getter, VersionType, get_soup

DOWNLOADS_PAGE = "https://www.dgidb.org/downloads"


class DGIGetter(Getter):
    """A getter for DGI."""

    name = "Drug Gene Interaction Database"
    version_type = VersionType.month
    date_version_fmt = "%Y-%b"

    def get(self):
        """Get the latest DGI version number."""
        soup = get_soup(DOWNLOADS_PAGE)
        # need to deconstruct graphql somehow?
        raise NotImplementedError


if __name__ == "__main__":
    DGIGetter.print()
