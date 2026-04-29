"""A getter for FlyBase."""

import re

from bioversions.utils import HUMAN_BROWSER_AGENT, Getter, VersionType, get_soup

__all__ = [
    "FlybaseGetter",
]

URL = "https://s3ftp.flybase.org/releases/"
PATTERN = re.compile(r"FB\d{4}_\d{2}")


class FlybaseGetter(Getter):
    """A getter for FlyBase."""

    bioregistry_id = "flybase"
    name = "FlyBase"
    homepage_fmt = "https://s3ftp.flybase.org/releases/FB{version}/"
    version_type = VersionType.month

    def get(self) -> str:
        """Get the latest FlyBase version."""
        soup = get_soup(URL, user_agent=HUMAN_BROWSER_AGENT)
        releases = [
            match.group().removeprefix("FB")
            for anchor_tag in soup.find_all("a", href=True)
            if (match := PATTERN.search(anchor_tag.text))
        ]
        if not releases:
            raise ValueError("flybase hit anti-scraping measurements")
        latest_version = max(releases)
        return latest_version


if __name__ == "__main__":
    FlybaseGetter.print()
