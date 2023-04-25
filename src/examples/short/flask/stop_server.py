"""
This is an example of how to stop a running flask server.
The solution here is pretty ugly (send kill signal to yourself),
but I have not found a nicer once.

References:
- https://stackoverflow.com/questions/15562446/how-to-stop-flask-application-without-using-ctrl-c
"""

from flask import Flask
from flask import request
import os
import signal

app = Flask("app")

@app.route("/")
def root():
    return "<html><body><h1>this is python with flask in a docker!<h1></body><html>"


@app.route('/stop_using_werkzeug')
def stop_using_wekzeug():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        return "Not running with the Werkzeug Server"
    func()
    return "Shutting down..."


@app.route('/crash')
def stopServer():
    os.kill(os.getpid(), signal.SIGINT)
    return "Server is shutting down..."

print(app.url_map)
app.run(port=8080, host="0.0.0.0")
