"""
This example shows how to remove the main flask messages.

References:
- https://stackoverflow.com/questions/14888799/disable-console-messages-in-flask-server
"""

import flask
import os

os.environ['WERKZEUG_RUN_MAIN'] = 'true'

app = flask.Flask(__name__)
app.run()
