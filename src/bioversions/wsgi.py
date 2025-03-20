"""A web application for listing database versions."""

from typing import Any

import flask
from flask_bootstrap import Bootstrap

from bioversions.sources import get_rows, resolve

app = flask.Flask(__name__)
Bootstrap(app)


@app.route("/")
def home() -> str:
    """Show the home page with a list of latest database versions."""
    return flask.render_template("home.html", rows=get_rows())


@app.route("/database/<name>.json")
def database(name: str) -> flask.Response:
    """Resolve information about a given database."""
    rv: dict[str, Any] = {"query": name}
    try:
        bioversion = resolve(name)
    except KeyError:
        rv["success"] = False
    else:
        rv["success"] = True
        rv["result"] = bioversion.model_dump()
    return flask.jsonify(rv)


if __name__ == "__main__":
    app.run()
