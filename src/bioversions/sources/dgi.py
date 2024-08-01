# -*- coding: utf-8 -*-

"""A getter for the `Drug Gene Interaction Database (DGI-DB) <http://www.dgidb.org>`_."""

import bs4
import dateutil.parser
import requests

from bioversions.utils import Getter, VersionType

GITHUB_PAGE = "https://github.com/dgidb/dgidb-v5"


class DGIGetter(Getter):
    """A getter for DGI."""

    name = "Drug Gene Interaction Database"
    version_type = VersionType.month
    date_version_fmt = "%Y-%b"

    def get(self):
        """Get the latest DGI version number."""
        res = requests.get(GITHUB_PAGE)
        soup = bs4.BeautifulSoup(res.content)
        time_tag = soup.find("relative-time")
        if time_tag is None:
            raise ValueError
        datetime_str = time_tag.attrs["datetime"]
        dt_obj = dateutil.parser.parse(datetime_str)
        version = dt_obj.strftime(self.date_version_fmt)
        return version


if __name__ == "__main__":
    DGIGetter.print()
