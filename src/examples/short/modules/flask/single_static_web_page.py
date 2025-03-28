""" single_static_web_page.py """

import flask


app = flask.Flask(__name__)


@app.route("/")
def hello():
    return "<html><body>Hello World!</body></html>"


app.run()
