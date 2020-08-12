"""
This example shows how to quiet flask logging down.

References:
- https://stackoverflow.com/questions/14888799/disable-console-messages-in-flask-server
"""

import flask
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = flask.Flask(__name__)
app.run()
