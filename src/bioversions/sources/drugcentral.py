# -*- coding: utf-8 -*-

"""A getter for DrugCentral."""

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    'DrugCentralGetter',
]

URL = 'https://drugcentral.org/download'


class DrugCentralGetter(Getter):
    """A getter for DrugCentral."""

    bioregistry_id = 'drugcentral'
    name = 'DrugCentral'
    date_version_fmt = '%m/%d/%Y'
    version_type = VersionType.date

    def get(self) -> str:
        """Get the latest DrugCentral version number."""
        soup = get_soup(URL)
        manifest = soup.find('section').find(**{'class': 'container'}).find('h4').find('a').find('u')
        return manifest.text.split(' ')[-1]


if __name__ == '__main__':
    DrugCentralGetter.print()
