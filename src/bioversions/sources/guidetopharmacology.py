# -*- coding: utf-8 -*-

"""A getter for GuideToPharmacology."""

import re
from datetime import datetime
from typing import Dict

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "GuideToPharmacologyGetter",
]

RE = re.compile(r"^.*(\d{4}\.\d+).*(\d{2}\/\d{2}\/\d{2}).*$")


class GuideToPharmacologyGetter(Getter):
    """A getter for the IUPHAR Guide to Pharmacology."""

    name = "Guide to Pharmacology"
    homepage_fmt = "https://www.guidetopharmacology.org/DATA/public_iuphardb_v{version}.zip"
    date_fmt = "%Y-%m-%d"
    version_type = VersionType.other

    def get(self) -> Dict[str, str]:
        """Get the latest Guide to Pharmacology version number."""
        downloads_url = "https://www.guidetopharmacology.org/download.jsp"
        soup = get_soup(downloads_url)
        text = soup.findAll("div", {"class": "contentboxfullhelp"})[4].div.ul.li.a.text
        search = RE.search(text)
        if search:
            grps = search.groups()
        else:
            raise ValueError(
                "Unable to extract version/date from Guide to Pharmacology Downloads page."
            )
        date = datetime.strftime(datetime.strptime(grps[1], "%d/%m/%y"), self.date_fmt)
        return {"version": grps[0], "date": date}


if __name__ == "__main__":
    GuideToPharmacologyGetter.print()
