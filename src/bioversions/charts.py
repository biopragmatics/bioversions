# -*- coding: utf-8 -*-


"""Generation of charts summarizing bioversions."""

import os
from collections import Counter

import click
import matplotlib.pyplot as plt
import seaborn as sns

from bioversions.sources import getters
from bioversions.utils import IMG

sns.set(style='whitegrid')


def verioning_pie_chart():
    """Make a pie chart with types of versions."""
    counts = Counter(
        getter.version_type.value
        for getter in getters
    )
    labels, counts = zip(*counts.most_common())
    fig, ax = plt.subplots()
    ax.pie(
        counts,
        labels=labels,
        autopct='%1.f%%',
        startangle=90,
        explode=[0.01 for _ in range(len(counts))],
        # shadow=True,
    )
    # fig.legend(fontsize='medium')
    fig.tight_layout()
    path = os.path.join(IMG, 'types.png')
    plt.savefig(path, dpi=300)
    plt.close(fig)


@click.command()
def charts():
    """Generate charts for bioversions."""
    verioning_pie_chart()


if __name__ == '__main__':
    charts()
