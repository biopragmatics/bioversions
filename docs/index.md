---
layout: home
---
This site and accompanying package are a resource for informing you what
the latest version of each biological database is.

<table>
<thead>
<tr>
    <th>Name</th>
    <th>Version</th>
    <th>Retrieved</th>
</tr>
</thead>
<tbody>
{% for entry in site.data.versions %}
    <tr>
        <td>{{ entry.name }}</td>
        <td>
            {% if entry.homepage %}<a href="{{ entry.homepage }}">{{ entry.version }} </a>{% else %}{{ entry.version }}{% endif %}
        </td>
        <td>{{ entry.retrieved }}</td>
    </tr>
{% endfor %}
</tbody>
</table>

## Download

This table can be downloaded as structured YAML from
[here](https://github.com/cthoyt/bioversions/blob/main/docs/_data/versions.yml).

## Programmatic Access

You can install the client with `pip install bioversions`.
The following code can be used in your own programs to access the latest database versions.

```python
import bioversions

assert bioversions.get_version('biogrid') == '4.2.192', 'This was true on Dec 5th, 2020!'
```

The source code can be found at [https://github.com/cthoyt/bioversions](https://github.com/cthoyt/bioversions).

## Adding More Databases

More databases can be added by sending a pull request to [cthoyt/bioversions](https://github.com/cthoyt/bioversions)
by following the [contribution guidelines](https://github.com/cthoyt/bioversions#-contributing).

## Database Updates

The database is automatically updated daily thanks to scheduled workflows in GitHub Actions.
The workflow's configuration can be found [here](https://github.com/cthoyt/bioversions/blob/main/.github/workflows/update.yml)
and the last run can be seen [here](https://github.com/cthoyt/bioversions/actions?query=workflow%3A%22Update+Database%22).
Further, a [changelog](https://github.com/cthoyt/bioversions/commits?author=actions-user) can be recapitulated from
the commits of the GitHub Actions bot.
