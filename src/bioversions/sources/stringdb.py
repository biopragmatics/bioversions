"""A getter for StringDB."""

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "StringDBGetter",
]


class StringDBGetter(Getter):
    """A getter for StringDB."""

    name = "StringDB"
    date_fmt = "%B %d, %Y"
    version_type = VersionType.other

    def get(self):
        """Get the latest StringDB version number."""
        soup = get_soup("https://string-db.org/cgi/access")
        table = soup.find(**{"class": "footer_access_archive_table"})
        rows = table.find_all(**{"class": "row"})
        version, date, link, _summary = (row.text for row in rows[1].find_all(**{"class": "cell"}))
        date = date[len("current: since ") :]
        return {"version": version, "date": date}


if __name__ == "__main__":
    StringDBGetter().print()
