# -*- coding: utf-8 -*-

"""A getter for MSigDB."""

from typing import Mapping

from bioversions.utils import Getter, get_soup

__all__ = [
    'MSigDBGetter',
]

URL = 'http://www.gsea-msigdb.org/gsea/msigdb/index.jsp'


class MSigDBGetter(Getter):
    """A getter for MSigDB."""

    name = 'MSigDB'

    def get(self) -> Mapping[str, str]:
        """Get the latest MSigDB version number."""
        soup = get_soup(URL)

        x = soup.find(text='Current Version')
        paragraph = x.parent.find_next_sibling('p')
        date = paragraph.text.strip()[len('MSigDB database v7.2 updated '):].split('.')[0]

        header = soup.find('h1')
        version = header.text.split(' ')[-1].lstrip('v')
        return dict(date=date, version=version)


if __name__ == '__main__':
    MSigDBGetter.print()
