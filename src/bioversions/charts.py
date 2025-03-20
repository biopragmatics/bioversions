"""Generation of charts summarizing bioversions."""

import os
from collections import Counter

import click
import matplotlib.pyplot as plt
import seaborn as sns

from bioversions.sources import get_getters
from bioversions.utils import IMG, VersionType

sns.set(style="whitegrid")


def version_types_pie_chart() -> None:
    """Make a pie chart with types of versions."""
    counter = Counter(
        "Missing" if getter.version_type is None else getter.version_type.value
        for getter in get_getters()
    )
    labels, counts = zip(*counter.most_common(), strict=False)
    fig, ax = plt.subplots()
    ax.pie(
        counts,
        labels=labels,
        autopct="%1.f%%",
        startangle=30,
        explode=[0.01 for _ in range(len(counts))],
    )
    fig.tight_layout()
    path = os.path.join(IMG, "version_types.svg")
    plt.savefig(path, dpi=300)
    plt.close(fig)


def verioning_date_formats_pie_chart() -> None:
    """Make a pie chart with types of date/month versions."""
    counter = Counter(
        getter.date_version_fmt
        for getter in get_getters()
        if getter.version_type in {VersionType.date, VersionType.month}
    )
    labels, counts = zip(*counter.most_common(), strict=False)
    fig, ax = plt.subplots()
    ax.pie(
        counts,
        labels=labels,
        autopct="%1.f%%",
        startangle=30,
        explode=[0.01 for _ in range(len(counts))],
    )
    fig.tight_layout()
    path = os.path.join(IMG, "version_date_types.svg")
    plt.savefig(path, dpi=300)
    plt.close(fig)


def has_release_url() -> None:
    """Make a pie chart for how many have a release URL."""
    counter = Counter(
        "Has Stable Version URL" if getter.homepage_fmt is not None else "No Stable Version URL"
        for getter in get_getters()
        if getter.version_type != VersionType.unversioned
    )
    labels, counts = zip(*counter.most_common(), strict=False)
    fig, ax = plt.subplots()
    ax.pie(
        counts,
        labels=labels,
        autopct="%1.f%%",
        startangle=30,
        explode=[0.01 for _ in range(len(counts))],
    )
    fig.tight_layout()
    path = os.path.join(IMG, "has_release_url.svg")
    plt.savefig(path, dpi=300)
    plt.close(fig)


@click.command()
def charts() -> None:
    """Generate charts for bioversions."""
    version_types_pie_chart()
    verioning_date_formats_pie_chart()
    has_release_url()


if __name__ == "__main__":
    charts()
