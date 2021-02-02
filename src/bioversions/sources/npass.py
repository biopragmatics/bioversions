# -*- coding: utf-8 -*-

"""A getter for NPASS."""

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    'NPASSGetter',
]


class NPASSGetter(Getter):
    """A getter for NPASS."""

    bioregistry_id = 'npass'
    name = 'NPASS'
    version_type = VersionType.semver_minor

    def get(self) -> str:
        """Get the latest NPASS version number."""
        soup = get_soup('http://bidd.group/NPASS/')
        for li in soup.find(name='footer').find(name='ul').findAll(name='li'):
            if li.text.startswith('Version:'):
                return li.text[len('Version: '):]


if __name__ == '__main__':
    NPASSGetter.print()
