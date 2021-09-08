---
layout: page
title: Summary
permalink: /summary/
---

## Version Types

The majority of databases use calendar versioning - this is highly skewed by the abundance of calendar versioning used
by ontologies from the OBO Foundry. Typically, ontologies accrue more content over time, so the concept of semantic
versions makes less sense. Databases whose schema may change or major new inclusions of data types could better benefit
from using semantic versioning.

<img src="https://raw.githubusercontent.com/biopragmatics/bioversions/main/docs/img/version_types.svg" alt="Version Types"/>

## Calendar Version Format

While the ISO-8601 format of `YYYY-MM-DD` is a standard, many databases manage to chose alternative date formats.

<img src="https://raw.githubusercontent.com/biopragmatics/bioversions/main/docs/img/version_date_types.svg" alt="Date Version Types"/>

## Has Stable URL for Each Release

It's not enough just to assign a version string to each release of data, but also for it to be possible to download a
given version of the data after it's been released. This chart shows (for versioned data) how many have stable URLs for
past versions of the data.

<img src="https://raw.githubusercontent.com/biopragmatics/bioversions/main/docs/img/has_release_url.svg" alt="Has Stable URL"/>
