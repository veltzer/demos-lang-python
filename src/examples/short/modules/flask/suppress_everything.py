"""
This example shows how to quiet flask logging down.

References:
- https://stackoverflow.com/questions/14888799/disable-console-messages-in-flask-server
"""

import logging
import os
import flask

log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)
os.environ["FLASK_ENV"] = "development"
os.environ["WERKZEUG_RUN_MAIN"] = "true"

app = flask.Flask(__name__)
app.run()
