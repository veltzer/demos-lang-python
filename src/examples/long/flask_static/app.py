"""
A simple web server
"""


from typing import TYPE_CHECKING

import flask

if TYPE_CHECKING:
    from flask.wrappers import Response

app = flask.Flask("app")
app.config["DEBUG"] = True
# static_folder = app.config["STATIC_FOLDER"]  # noqa: ERA001  teaching: kept in the comment for the reader
print(f"{app.static_folder=}")


@app.route("/")
def index() -> Response:
    return app.send_static_file("index.html")


if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0")
