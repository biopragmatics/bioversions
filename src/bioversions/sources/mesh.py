"""A getter for MeSH."""

import datetime
import ftplib
import logging

from bioversions.utils import Getter, VersionType

__all__ = [
    "MeshGetter",
]

logger = logging.getLogger(__name__)

#: In 2024 and before, these were .gz, but after
#: became .xml files
SUFFIXES = [".xml", ".xml.gz", ".gz"]


class MeshGetter(Getter):
    """A getter for MeSH."""

    bioregistry_id = "mesh"
    name = "MeSH"
    homepage_fmt = "ftp://nlmpubs.nlm.nih.gov/online/mesh/{version}"
    version_type = VersionType.year

    def get(self):
        """Get the latest MeSH version number."""
        try:
            with ftplib.FTP("nlmpubs.nlm.nih.gov") as ftp:
                ftp.login()
                ftp.cwd("/online/mesh/MESH_FILES/xmlmesh/")
                names = [name for name, _ in ftp.mlsd()]

        except Exception as e:
            logger.warning(
                "could not look up MeSH version, falling back to current year. exception: %s", e
            )
            return str(datetime.date.today().year)

        for name in names:
            for suffix in SUFFIXES:
                if name.startswith("desc") and name.endswith(suffix):
                    return name[len("desc") : -len(suffix)]

        raise ValueError("unable to parse results returned from MeSH FTP")


if __name__ == "__main__":
    MeshGetter.print()
