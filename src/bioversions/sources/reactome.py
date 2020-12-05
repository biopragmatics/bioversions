from bioversions.utils import Getter, get_soup

URL = 'https://reactome.org/'


class ReactomeGetter(Getter):
    name = 'Reactome'

    def get(self):
        """Get the latest BioGRID version number."""
        soup = get_soup(URL)
        manifest = soup.find(id='fav-portfoliowrap')
        header = manifest.find('h3')
        return header.text.split()[1]


if __name__ == '__main__':
    ReactomeGetter.print()
