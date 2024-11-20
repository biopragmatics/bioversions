"""A getter for DrugCentral."""

from contextlib import closing

from bioversions.utils import Getter, VersionType

__all__ = [
    "DrugCentralGetter",
]

HOST = "unmtid-dbs.net"
PORT = 5433
USER = "drugman"
PASSWORD = "dosage"  # noqa:S105
DBNAME = "drugcentral"
PARAMS = {"dbname": DBNAME, "user": USER, "password": PASSWORD, "host": HOST, "port": PORT}


class DrugCentralGetter(Getter):
    """A getter for DrugCentral."""

    bioregistry_id = "drugcentral"
    name = "DrugCentral"
    date_fmt = "%Y-%m-%d"
    version_type = VersionType.date

    def get(self):
        """Get the latest DrugCentral version number."""
        import psycopg2

        with closing(psycopg2.connect(**PARAMS)) as conn:
            with closing(conn.cursor()) as cur:
                cur.execute("SELECT version, dtime FROM public.dbversion")
                version, dtime = cur.fetchone()

        # TODO update return format to allow datetime type
        return {
            "version": str(version),
            "date": dtime.strftime(self.date_fmt),
        }


if __name__ == "__main__":
    DrugCentralGetter.print()
