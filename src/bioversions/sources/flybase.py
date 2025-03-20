"""A getter for FlyBase."""

import re

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "FlybaseGetter",
]

URL = "http://flybase-ftp.s3-website-us-east-1.amazonaws.com/releases/index.html"
PATTERN = re.compile(r"FB\d{4}_\d{2}")


class FlybaseGetter(Getter):
    """A getter for FlyBase."""

    bioregistry_id = "flybase"
    name = "FlyBase"
    homepage_fmt = "http://flybase-ftp.s3-website-us-east-1.amazonaws.com/releases/FB{version}/"
    version_type = VersionType.month

    def get(self):
        """Get the latest flybase version number."""
        soup = get_soup(URL)

        releases = []
        # We check links to find ones that look like releases
        for anchor_tag in soup.find_all("a", href=True):
            match = PATTERN.search(anchor_tag.text)
            if match:
                releases.append(match.group().removeprefix("FB"))
        latest_version = max(releases)
        return latest_version


if __name__ == "__main__":
    FlybaseGetter.print()
