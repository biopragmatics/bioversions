# -*- coding: utf-8 -*-

"""A getter for FlyBase."""

import ftplib

from bioversions.utils import Getter, VersionType

__all__ = [
    "FlybaseGetter",
]


class FlybaseGetter(Getter):
    """A getter for FlyBase."""

    bioregistry_id = "flybase"
    name = "FlyBase"
    homepage_fmt = "http://ftp.flybase.net/releases/FB{version}/"
    version_type = VersionType.date

    def get(self):
        """Get the latest flybase version number."""
        with ftplib.FTP("ftp.flybase.net") as ftp:
            ftp.login()
            ftp.cwd("releases")
            for name in sorted(ftp.nlst(), reverse=True):
                if name.startswith("FB2"):
                    return name[len("FB") :]
        raise ValueError


if __name__ == "__main__":
    FlybaseGetter.print()
