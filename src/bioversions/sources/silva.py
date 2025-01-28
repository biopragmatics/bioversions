"""A getter for SILVA."""

import datetime

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "SILVAGetter",
]

URL = "https://www.arb-silva.de/fileadmin/silva_databases/current/VERSION.txt"


class SILVAGetter(Getter):
    """A getter for the SILVA."""

    bioregistry_id = "silva.taxon"
    name = "SILVA ribosomal RNA database"
    version_type = VersionType.sequential
    homepage_fmt = "https://www.arb-silva.de/"

    def get(self):
        """Get the latest SILVA version number from VERSION.txt."""
        res = requests.get(URL, timeout=15)

        # Get version from the content
        version = res.text.strip()

        # Get date from the Last-Modified header
        date_str = res.headers.get("Last-Modified")
        if date_str:
            date = datetime.datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %Z").strftime(
                self.date_fmt
            )
        else:
            date = None

        return {"version": version, "date": date}


if __name__ == "__main__":
    SILVAGetter.print()
