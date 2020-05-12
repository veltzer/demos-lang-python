#!/usr/bin/env python

"""
Minimal running flask application
- It will listen to port 5000
- It will only listen to incoming requests from localhost.
- So these will work:
    $ wget localhost:5000
    $ wget 127.0.0.1:5000
- It will not listen to any other ip. If you have external
- ip [ip] then this *will not work*:
    $ wget [ip]:5000
- This will also issue a warning about not using an efficient
    application framework to run flask with.
- This will also issue some informational messages about
    flask.
"""

import flask

app = flask.Flask(__name__)
app.run()
