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
    version_type = VersionType.date

    def get(self):
        """Get the latest flybase version number."""
        soup = get_soup(URL)

        releases = []
        # We check links to find ones that look like releases
        for a_tag in soup.find_all("a", href=True):
            match = PATTERN.search(a_tag.text)
            if match:
                # Strip off the leading FB here
                releases.append(match.group()[2:])
        latest_version = max(releases)
        return latest_version


if __name__ == "__main__":
    FlybaseGetter.print()
