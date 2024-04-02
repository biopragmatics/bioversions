# -*- coding: utf-8 -*-

"""A getter for GuideToPharmacology."""

import re
from datetime import datetime
from typing import Dict

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "GuideToPharmacologyGetter",
]

URL = "https://www.guidetopharmacology.org/download.jsp"
RE = re.compile(r"^.*(\d{4}\.\d+).*(\d{2}\/\d{2}\/\d{2}).*$")


class GuideToPharmacologyGetter(Getter):
    """A getter for the IUPHAR Guide to Pharmacology."""

    name = "Guide to Pharmacology"
    homepage_fmt = "https://www.guidetopharmacology.org/DATA/public_iuphardb_v{version}.zip"
    date_fmt = "%Y-%m-%d"
    version_type = VersionType.year_minor
    collection = ["iuphar.family", "iuphar.ligand", "iuphar.receptor"]

    def get(self) -> Dict[str, str]:
        """Get the latest Guide to Pharmacology version number."""
        soup = get_soup(URL)
        text = soup.findAll("div", {"class": "contentboxfullhelp"})[4].div.ul.li.a.text
        search = RE.search(text)
        if not search:
            raise ValueError(
                "Unable to extract version/date from Guide to Pharmacology Downloads page."
            )
        grps = search.groups()
        date = datetime.strftime(datetime.strptime(grps[1], "%d/%m/%y"), self.date_fmt)
        return {"version": grps[0], "date": date}


if __name__ == "__main__":
    GuideToPharmacologyGetter.print()
