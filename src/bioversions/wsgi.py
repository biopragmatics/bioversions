"""A web application for listing database versions."""

import flask
from fastapi import FastAPI
from flask_bootstrap import Bootstrap4
from pydantic import BaseModel

from bioversions import VersionResult
from bioversions.sources import get_rows, resolve
from a2wsgi import WSGIMiddleware

fastapi_app = FastAPI()

app = flask.Flask(__name__)
Bootstrap4(app)

fastapi_app.mount("/", WSGIMiddleware(app))


@app.route("/")
def home() -> str:
    """Show the home page with a list of latest database versions."""
    return flask.render_template("home.html", rows=get_rows())


class VersionResponse(BaseModel):
    """A model for a response."""

    query: str
    success: bool
    result: VersionResult | None


@fastapi_app.get("/database/<name>.json", response_model=VersionResponse)
def database(name: str) -> VersionResponse:
    """Resolve information about a given database."""
    try:
        result = resolve(name)
    except KeyError:
        success = False
        result = None
    else:
        success = True

    return VersionResponse(query=name, success=success, result=result)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(fastapi_app, port=8777, host="0.0.0.0")  # noqa:S104
