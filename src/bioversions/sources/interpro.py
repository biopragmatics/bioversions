# -*- coding: utf-8 -*-

"""A getter for InterPro."""

import re

import requests

from bioversions.utils import Getter, VersionType, _get_ftp_version

__all__ = [
    "InterProGetter",
]

SOLVE_RE = re.compile(r"(\d)(st|nd|rd|th)")


class InterProGetter(Getter):
    """A getter for InterPro."""

    bioregistry_id = "interpro"
    name = "InterPro"
    homepage_fmt = "ftp://ftp.ebi.ac.uk/pub/databases/interpro/{version}/"
    date_fmt = "%d %B %Y"
    version_type = VersionType.semver_minor

    def get(self):
        """Get the latest InterPro version number."""
        version = _get_ftp_version("ftp.ebi.ac.uk", "pub/databases/interpro/")

        with requests.Session() as session:
            res = session.get(
                "ftp://ftp.ebi.ac.uk/pub/databases/interpro/current/release_notes.txt"
            )
            for line in res.iter_lines():
                line = line.decode("utf8").strip()
                if line.startswith("Release") and not line.startswith("Release Notes"):
                    return dict(version=version, date=_process_line(line))
        raise ValueError


def _process_line(s: str) -> str:
    return SOLVE_RE.sub(r"\1", s.split(",")[1].strip())


if __name__ == "__main__":
    InterProGetter.print()
