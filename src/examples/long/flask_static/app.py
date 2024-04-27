#!/usr/bin/env python3

"""
A simple web server
"""


import flask


app = flask.Flask("app")
app.config["DEBUG"] = True
# static_folder = app.config["STATIC_FOLDER"]
print(f"{app.static_folder=}")


@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0")
