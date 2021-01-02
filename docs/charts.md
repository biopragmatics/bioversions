---
layout: page title: Charts permalink: /charts/
---

## Version Types

The majority of databases use calendar versioning - this is highly skewed by the abundance of calendar versioning used
by ontologies from the OBO Foundry. Typically, ontologies accrue more content over time, so the concept of semantic
versions makes less sense. Databases whose schema may change or major new inclusions of data types could better benefit
from using semantic versioning.

<img src="https://raw.githubusercontent.com/cthoyt/bioversions/main/docs/img/version_types.png" alt="Version Types"/>

## Calendar Version Format

While the ISO-8601 format of `YYYY-MM-DD` is a standard, many databases manage to chose alternative date formats.

<img src="https://raw.githubusercontent.com/cthoyt/bioversions/main/docs/img/version_date_types.png" alt="Date Version Types"/>
