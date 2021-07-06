# -*- coding: utf-8 -*-

"""A getter for MSigDB."""

from typing import Mapping

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "MSigDBGetter",
]

URL = "http://www.gsea-msigdb.org/gsea/msigdb/index.jsp"


class MSigDBGetter(Getter):
    """A getter for MSigDB."""

    bioregistry_id = "msigdb"
    name = "MSigDB"
    homepage_fmt = "https://data.broadinstitute.org/gsea-msigdb/msigdb/release/{version}"
    date_fmt = "%B %Y"
    version_type = VersionType.month

    def get(self) -> Mapping[str, str]:
        """Get the latest MSigDB version number."""
        soup = get_soup(URL)

        header = soup.find("h1")
        version = header.text.split(" ")[-1].lstrip("v")

        x = soup.find(text="Current Version")
        paragraph = x.parent.find_next_sibling("p")
        date = paragraph.text.strip()[len(f"MSigDB database v{version} updated ") :].split(".")[0]

        return dict(date=date, version=version)


if __name__ == "__main__":
    MSigDBGetter.print()
