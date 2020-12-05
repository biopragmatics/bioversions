# Bioversions

What's the current version for each biological database?

## Installation

`pip install -e .`

## Usage

```python
import bioversions

bioversion = bioversions.resolve('biogrid')
assert bioversion.version == '4.2.192', 'This was true on Dec 5th, 2020!'
```

## Web Application

Run the web application in your shell with

```bash
$ bioversions
```

Options can be listed with `bioversions --help`.

You can navigate to http://localhost:5000 to see all versions
as HTML or programmatically resolve given databases with the
`http://localhost:5000/database/<name>` endpoint like in the
following:

```python
import requests

res = requests.get('http://localhost:5000/database/biogrid').json()
assert res['success']
assert res['result']['name'] == 'BioGRID'
assert res['result']['version'] == '4.2.192', 'This was true on Dec 5th, 2020!'
```

## Contributing

To add more databases to the list, you can create a new submodule of
`bioversions.sources` and extend the `bioversions.utils.Getter` class
to identify the most recent version for your target database. See
`bioversions.sources.biogrid` as an example.
