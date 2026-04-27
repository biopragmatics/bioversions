"""A getter for the `Drug Gene Interaction Database (DGI-DB) <http://www.dgidb.org>`_."""

import dateutil.parser

from bioversions.utils import Getter, VersionType, find, get_soup

GITHUB_PAGE = "https://github.com/dgidb/dgidb-v5"


class DGIGetter(Getter):
    """A getter for DGI."""

    name = "Drug Gene Interaction Database"
    version_type = VersionType.month
    date_version_fmt = "%Y-%b"

    def get(self) -> str:
        """Get the latest DGI version number."""
        soup = get_soup(GITHUB_PAGE)
        time_tag = find(soup, "relative-time")
        datetime_str = time_tag.attrs["datetime"]
        if not isinstance(datetime_str, str):
            raise ValueError
        dt_obj = dateutil.parser.parse(datetime_str)
        version = dt_obj.strftime(self.date_version_fmt)
        return version


if __name__ == "__main__":
    DGIGetter.print()
