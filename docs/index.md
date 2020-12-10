---
layout: home
---
<table>
<thead>
<tr>
    <th>Name</th>
    <th>Version</th>
    <th>Updated</th>
</tr>
</thead>
<tbody>
{% for entry in site.data.versions %}
    <tr>
        <td>{{ entry.name }}</td>
        <td>
            {% if entry.homepage %}<a href="{{ entry.homepage }}">{{ entry.version }} </a>{% else %}{{ entry.version }}{% endif %}
        </td>
        <td>{{ entry.updated }}</td>
    </tr>
{% endfor %}
</tbody>
</table>
