"""
mservice_b.py
"""

from flask import Flask, request

app = Flask(__name__)


@app.route("/add")
def add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(a + b)


app.run(port=8081)
