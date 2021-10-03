# -*- coding: utf-8 -*-

"""A web application for listing database versions."""

from typing import Any, Dict

import flask
from flask_bootstrap import Bootstrap

from bioversions.sources import get_rows, resolve

app = flask.Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    """Show the home page with a list of latest database versions."""
    return flask.render_template("home.html", rows=get_rows())


@app.route("/database/<name>.json")
def database(name: str):
    """Resolve information about a given database."""
    rv: Dict[str, Any] = dict(query=name)
    try:
        bioversion = resolve(name)
    except KeyError:
        rv["success"] = False
    else:
        rv["success"] = True
        rv["result"] = bioversion.dict()
    return flask.jsonify(rv)


if __name__ == "__main__":
    app.run()
