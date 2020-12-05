from bioversions.utils import Getter, get_soup

URL = 'https://downloads.thebiogrid.org/BioGRID/Latest-Release/'


class BioGRIDGetter(Getter):
    name = 'BioGRID'
    homepage_fmt = 'https://downloads.thebiogrid.org/BioGRID/Release-Archive/BIOGRID-{version}'

    def get(self) -> str:
        """Get the latest BioGRID version number."""
        soup = get_soup(URL)
        manifest = soup.find(id='manifestDesc')
        header = manifest.find('h2')
        return header.text[len('BioGRID Release '):]


if __name__ == '__main__':
    BioGRIDGetter.print()
