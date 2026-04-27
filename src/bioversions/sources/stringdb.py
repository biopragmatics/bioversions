"""A getter for StringDB."""

from bioversions.utils import Getter, ReleaseDict, VersionType, find_soup_tag, get_soup

__all__ = [
    "StringDBGetter",
]


class StringDBGetter(Getter):
    """A getter for StringDB."""

    name = "StringDB"
    date_fmt = "%B %d, %Y"
    version_type = VersionType.other

    def get(self) -> ReleaseDict:
        """Get the latest StringDB version number."""
        soup = get_soup("https://string-db.org/cgi/access")
        table = find_soup_tag(soup, class_="footer_access_archive_table")
        rows = table.find_all(class_="row")
        row = rows[1]
        version, date, _address, _content = row.find_all(class_="cell")
        if not isinstance(version.text, str) or not version.text:
            raise ValueError
        if not isinstance(date.text, str) or not date.text:
            raise ValueError
        return {"version": version.text, "date": date.text[len("current: since ") :]}


if __name__ == "__main__":
    StringDBGetter().print()
