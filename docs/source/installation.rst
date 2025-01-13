Installation
============
The most recent release can be installed from
`PyPI <https://pypi.org/project/bioversions>`_ with:

.. code-block:: shell

    python3 -m pip install bioversions

The most recent code and data can be installed directly from GitHub with:

.. code-block:: shell

    python3 -m pip install git+https://github.com/biopragmatics/bioversions.git

To install in development mode, use the following:

.. code-block:: shell

    git clone git+https://github.com/biopragmatics/bioversions.git
    cd bioversions
    UV_PREVIEW=1 python3 -m pip install -e .

Note that the ``UV_PREVIEW`` environment variable is required to be
set until the uv build backend becomes a stable feature.
