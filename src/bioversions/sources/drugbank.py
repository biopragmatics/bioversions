# -*- coding: utf-8 -*-

"""A getter for DrugBank."""

from bioversions.utils import Getter, get_soup

__all__ = [
    'DrugBankGetter',
]

URL = 'https://go.drugbank.com/releases/latest'


class DrugBankGetter(Getter):
    """A getter for DrugBank."""

    name = 'DrugBank'
    homepage = 'https://go.drugbank.com/releases/{version}'

    def get(self):
        """Get the latest DrugBank version number."""
        soup = get_soup(URL)
        manifest = soup.find(**{'class': 'download-table'}).find('table').find('tbody').find('tr')
        manifest = list(manifest)
        date = manifest[1].text
        version = manifest[2].text
        return dict(date=date, version=version)


if __name__ == '__main__':
    DrugBankGetter.print()
