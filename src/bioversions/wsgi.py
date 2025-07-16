"""A web application for listing database versions."""

import flask
from fastapi import FastAPI
from flask_bootstrap import Bootstrap
from pydantic import BaseModel

from bioversions import VersionResult
from bioversions.sources import get_rows, resolve

fastapi_app = FastAPI()

app = flask.Flask(__name__)
Bootstrap(app)


@app.route("/")
def home() -> str:
    """Show the home page with a list of latest database versions."""
    return flask.render_template("home.html", rows=get_rows())


class Respon(BaseModel):
    """A model for a response."""

    query: str
    success: bool
    result: VersionResult | None


@fastapi_app.get("/database/<name>.json", response_model=Respon)
def database(name: str) -> Respon:
    """Resolve information about a given database."""
    try:
        result = resolve(name)
    except KeyError:
        success = False
        result = None
    else:
        success = True

    return Respon(query=name, success=success, result=result)


if __name__ == "__main__":
    app.run()
