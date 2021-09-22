---
layout: home
---
<p align="center">
  <img src="https://raw.githubusercontent.com/biopragmatics/bioversions/main/docs/source/logo.png" height="150">
</p>

This site and accompanying package are a resource for informing you what the latest version of each biological database
is. Last updated on {{ site.data.versions.annotations.date }} (revision {{ site.data.versions.annotations.revision }})
by {{ site.data.versions.annotations.author }}.

This site also includes [Bioschemas](https://bioschemas.org/) annotations, which
aims to improve the findability of life sciences resources such as datasets,
software, and training materials. These annotations can either appear on the
original site, or on a website (like this one) that indexes it or provides
additional information. The further information here, for example, is the link
to the BioRegistry. The JSON-LD annotation will make it easier for other
tools to recognize the content of the table. This includes the [Google Dataset
finder](https://datasetsearch.research.google.com/), besides Bioschemas itself.

Legend: 📥 means the resource reports the date of each release, 📅 means the date of release was inferred based on the
date when the latest version was retrieved, 💡 means the date was inferred by the version string.

<table id="versions-table">
<thead>
<tr>
    <th>Prefix</th>
    <th>Name</th>
    <th>Version</th>
    <th>Date</th>
    <th></th>
</tr>
</thead>
<tbody>
{% for entry in site.data.versions.database %}
    {% assign latest = entry.releases | last %}
    <tr>
        <td>
        {% if entry.prefix %}
            <script type="application/ld+json">
            {
                "@context": "https://schema.org",
                "@type": "Dataset",
                "@id": "https://bioregistry.io/{{ entry.prefix }}",
                "name": "{{ entry.name }}",
                "version": "{{ latest.version }}"
            }
            </script>
            <a href="https://bioregistry.io/{{ entry.prefix }}"><code>{{ entry.prefix }}</code></a>
        {% elsif entry.key %}
            {% comment %} 
               todo: add Bioschemas for non-prefixed resources. 
               will be easier after https://github.com/biopragmatics/bioversions/issues/13
            {% endcomment %}
            {{ entry.key }}
        {% endif %}
        </td>
        <td>{{ entry.name }}</td>
        <td>
            {% if latest.homepage %}<a href="{{ latest.homepage }}">{{ latest.version }} </a>{% else %}{{ latest.version }}{% endif %}
        </td>
        {% if latest.date %}<td>{{ latest.date }}</td><td>📥</td>
        {% elsif entry.vtype == "date" %}<td>-</td><td>💡</td>
        {% else %}<td>{{ latest.retrieved }}</td><td>📅</td>
        {% endif %}
    </tr>
{% endfor %}
</tbody>
</table>

<script>
$(document).ready(function () {
   $("#versions-table").DataTable();
});
</script>

## Adding More Databases

More databases can be added by sending a pull request to [biopragmatics/bioversions](https://github.com/biopragmatics/bioversions)
by following the [contribution guidelines](https://github.com/biopragmatics/bioversions#-contributing).

Databases are added by the following priority (high to low):

1. By request or contribution
2. Databases useful for the [PyOBO](https://github.com/pyobo/pyobo) project, aiming to convert all biomedical controlled
   vocabularies into OBO for general reuse
3. Databases useful for the [Bio2BEL](https://github.com/bio2bel/bio2bel) project, aiming to convert all biological
   databases into the [Biological Expression Language](https://biological-expression-language.github.io/) for general
   reuse and Bio2BEL projects
4. Databases appearing in the Bioregistry, OLS, OBO Foundry, or MIRIAM
5. Databases tweeted by the International Society of Biocuration ([@biocurator](https://twitter.com/biocurator))
6. Databases I've seen during project work
7. Serendipity!

## Database Updates

The database is automatically updated daily thanks to scheduled workflows in GitHub Actions. The workflow's
configuration can be found [here](https://github.com/biopragmatics/bioversions/blob/main/.github/workflows/update.yml)
and the last run can be
seen [here](https://github.com/biopragmatics/bioversions/actions?query=workflow%3A%22Update+Database%22). Further,
a [changelog](https://github.com/biopragmatics/bioversions/commits?author=actions-user) can be recapitulated from the commits
of the GitHub Actions bot.
