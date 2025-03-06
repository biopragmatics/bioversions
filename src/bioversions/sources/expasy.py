"""A getter for ExPASy."""

from datetime import datetime

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "ExPASyGetter",
]

URL = "https://ftp.expasy.org/databases/enzyme/enzuser.txt"


class ExPASyGetter(Getter):
    """A getter for ExPASy."""

    bioregistry_id = "ec"
    name = "ExPASy"
    version_type = VersionType.date

    def get(self) -> str:
        """Get the latest ExPASy version number."""
        s = requests.Session()
        res = s.get(URL, stream=True)
        li = res.iter_lines()
        next(li)
        next(li)
        r = next(li).decode("utf8").strip()[len("Release of ") :]
        return datetime.strptime(r, "%d-%b-%Y").strftime("%Y-%m-%d")


if __name__ == "__main__":
    ExPASyGetter.print()
