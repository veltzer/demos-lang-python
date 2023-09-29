import os
import flask

app = flask.Flask(__name__)


@app.route("/")
def hello():
    return "<html><body>Hello World!</body></html>"


@app.route("/shutdown")
def shutdown():
    # suicide
    os.kill(os.getpid(), 9)
    return ""


app.run(port=8080)
