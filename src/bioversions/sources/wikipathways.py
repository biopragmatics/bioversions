# -*- coding: utf-8 -*-

"""A getter for WikiPathways."""

from bioversions.utils import Getter, get_soup

__all__ = [
    'WikiPathwaysGetter',
]

URL = 'http://data.wikipathways.org/current/index/'


class WikiPathwaysGetter(Getter):
    """A getter for WikiPathways."""

    name = 'WikiPathways'
    homepage_fmt = 'http://data.wikipathways.org/{version}/'

    def get(self):
        """Get the latest WikiPathways version number."""
        soup = get_soup(URL)
        element = soup.find('tbody').find('tr').find('td').find('a')
        return element.text.split('-')[1]


if __name__ == '__main__':
    WikiPathwaysGetter.print()
