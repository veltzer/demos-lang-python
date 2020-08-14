"""
This is an exmple of how to get ridd of the "development" message.
Another way is to run a WSGI server which is not flask (say gevent or something).

References:
- https://stackoverflow.com/questions/50284753/warning-message-while-running-flask
"""

import flask
import os

app = flask.Flask(__name__)
os.environ["FLASK_ENV"] = "development"


@app.route("/")
def hello():
    return "Hello, World!"


app.run()
