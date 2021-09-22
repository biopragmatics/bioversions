# -*- coding: utf-8 -*-

"""A getter for the NCI Thesaurus."""

from ..utils import Getter, VersionType, get_soup
import re
from typing import Dict

__all__ = [
    "NCItGetter",
]

URL = "https://ncithesaurus.nci.nih.gov/ncitbrowser/"
PATTERN = re.compile(r"Version:([0-9]{2}\.[0-9]{2}[a-z]) "
                     r"\(Release date:([0-9]{4}-[0-9]{2}-[0-9]{2})")

class NCItGetter(Getter):
    """A getter for the NCI Thesaurus."""

    bioregistry_id = "ncit"
    name = "NCIt"
    date_fmt = "%Y-%m-%d"
    version_type = VersionType.other

    def get(self) -> Dict[str, str]:
        """Get the latest NCIt version number."""
        soup = get_soup(URL)
        version_str = soup.find('span', {'class': 'vocabularynamelong_ncit'}).contents[0]
        match = re.search(PATTERN, version_str)
        return {
            "version": match.group(1),
            "date": match.group(2),
        }


if __name__ == "__main__":
    NCItGetter.print()
