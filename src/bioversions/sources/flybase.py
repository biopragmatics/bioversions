"""A getter for FlyBase."""

import re

from bs4 import BeautifulSoup
import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "FlybaseGetter",
]


class FlybaseGetter(Getter):
    """A getter for FlyBase."""

    bioregistry_id = "flybase"
    name = "FlyBase"
    homepage_fmt = (
        "http://flybase-ftp.s3-website-us-east-1.amazonaws.com/releases/FB{version}/"
    )
    version_type = VersionType.date

    def get(self):
        """Get the latest flybase version number."""
        res = requests.get(
            "http://flybase-ftp.s3-website-us-east-1.amazonaws.com/releases/index.html",
            timeout=15,
        )
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        release_pattern = re.compile(r"FB\d{4}_\d{2}")
        releases = []
        # We check links to find ones that look like releases
        for a_tag in soup.find_all("a", href=True):
            match = release_pattern.search(a_tag.text)
            if match:
                # Strip off the leading FB here
                releases.append(match.group()[2:])
        latest_version = sorted(releases, reverse=True)[0]
        return latest_version


if __name__ == "__main__":
    FlybaseGetter.print()
