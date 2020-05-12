#!/usr/bin/env python

"""
This example shows how to remove the static path from flasks url map.

References:
"""

import flask

app = flask.Flask(__name__)
print(app.url_map)
# remove the entry (TBD)
print(app.url_map)
