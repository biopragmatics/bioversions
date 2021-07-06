<p align="center">
  <img src="https://github.com/cthoyt/bioversions/raw/main/docs/source/logo.png" height="150">
</p>

<h1 align="center">
    Bioversions
</h1>

<p align="center">
    <a href="https://pypi.org/project/bioversions">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/bioversions" />
    </a>
    <a href="https://pypi.org/project/bioversions">
        <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/bioversions" />
    </a>
    <a href="https://github.com/cthoyt/bioversions/blob/main/LICENSE">
        <img alt="PyPI - License" src="https://img.shields.io/pypi/l/bioversions" />
    </a>
    <a href="https://zenodo.org/badge/latestdoi/318852276">
        <img src="https://zenodo.org/badge/318852276.svg" alt="DOI" />
    </a>
    <a href="https://github.com/psf/black">
        <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black">
    </a>
</p>

What's the current version for each biological database?

A daily updated static listing of all current versions (that are incorporated) can be found at
https://cthoyt.github.io/bioversions.

## 🚀 Installation

```bash
$ pip install bioversions
```

## 💪 Usage

```python
import bioversions

assert bioversions.get_version('biogrid') == '4.2.192', 'This was true on Dec 5th, 2020!'

# If you want more information, use the resolve() function
bioversion = bioversions.resolve('biogrid')
assert bioversion.version == '4.2.192'
```

By default, the results are cached and only refreshed once per day with the help
of [`cachier`](https://github.com/shaypal5/cachier). The cache is stored in `~/.data/bioversions`. The cache location
can be overridden by setting the
`BIOVERSIONS_HOME` environment variable via [`pystow`](https://github.com/cthoyt/pystow).

## 🌐 Web Application

While https://cthoyt.github.io/bioversions provides a daily updated static listing of the database, you can run a
dynamic version with an API from your shell with:

```bash
$ bioversions web
```

Options can be listed with `bioversions web --help`.

You can navigate to http://localhost:5000 to see all versions as HTML or programmatically resolve given databases with
the
`http://localhost:5000/database/<name>` endpoint like in the following:

```python
import requests

res = requests.get('http://localhost:5000/database/biogrid').json()
assert res['success']
assert res['result']['name'] == 'BioGRID'
assert res['result']['version'] == '4.2.192', 'This was true on Dec 5th, 2020!'
```

## CLI Usage

You can use `bioversions get` to incorporate the latest versions in your shell scripts or REPL usage like in:

```bash
$ wget "https://downloads.thebiogrid.org/Download/BioGRID/Release-Archive/BIOGRID-$(bioversions get biogrid)/BIOGRID-ALL-$(bioversions get biogrid).mitab.zip"
```

## 🙏 Contributing

To add more databases to the list, you can create a new submodule of
`bioversions.sources` and extend the `bioversions.utils.Getter` class to identify the most recent version for your
target database. See
`bioversions.sources.biogrid` as an example.
