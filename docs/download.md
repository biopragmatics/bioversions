---
layout: page
title: Download
permalink: /download/
---
This table can be downloaded as structured YAML from
[here](https://github.com/biopragmatics/bioversions/blob/main/docs/_data/versions.yml).

## License

These data are available under the CC0 1.0 Universal License.

## Programmatic Access

You can install the client with `pip install bioversions`.
The following code can be used in your own programs to access the latest database versions.

```python
import bioversions

assert bioversions.get_version('biogrid') == '4.2.192', 'This was true on Dec 5th, 2020!'
```

The source code can be found at [https://github.com/biopragmatics/bioversions](https://github.com/biopragmatics/bioversions).
