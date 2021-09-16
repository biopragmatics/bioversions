# -*- coding: utf-8 -*-

"""A getter for PomBase."""

import ftplib

from bioversions.utils import Getter, VersionType

__all__ = [
    "PombaseGetter",
]


class PombaseGetter(Getter):
    """A getter for PomBase."""

    bioregistry_id = "pombase"
    name = "PomBase"
    date_version_fmt = "%Y-%m-%d"
    homepage_fmt = "https://www.pombase.org/data/releases/pombase-{version}/"
    version_type = VersionType.date

    def get(self):
        """Get the latest pombase version number."""
        with ftplib.FTP("www.pombase.org") as ftp:
            ftp.login()
            ftp.cwd("releases")
            for name in sorted(ftp.nlst(), reverse=True):
                if name.startswith("pombase-"):
                    return name[len("pombase-") :]
        raise ValueError


if __name__ == "__main__":
    PombaseGetter.print()
