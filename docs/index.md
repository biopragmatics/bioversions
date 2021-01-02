---
layout: home
---
<p align="center">
  <img src="https://raw.githubusercontent.com/cthoyt/bioversions/main/docs/source/logo.png" height="150">
</p>

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
    {% assign latest = entry.releases | last %}
    <tr>
        <td>{{ entry.name }}</td>
        <td>
            {% if latest.homepage %}<a href="{{ latest.homepage }}">{{ latest.version }} </a>{% else %}{{ latest.version }}{% endif %}
        </td>
        <td>{{ latest.retrieved }}</td>
    </tr>
{% endfor %}
</tbody>
</table>

## Adding More Databases

More databases can be added by sending a pull request to [cthoyt/bioversions](https://github.com/cthoyt/bioversions)
by following the [contribution guidelines](https://github.com/cthoyt/bioversions#-contributing).

## Database Updates

The database is automatically updated daily thanks to scheduled workflows in GitHub Actions.
The workflow's configuration can be found [here](https://github.com/cthoyt/bioversions/blob/main/.github/workflows/update.yml)
and the last run can be seen [here](https://github.com/cthoyt/bioversions/actions?query=workflow%3A%22Update+Database%22).
Further, a [changelog](https://github.com/cthoyt/bioversions/commits?author=actions-user) can be recapitulated from
the commits of the GitHub Actions bot.
