"""
mservice_b.py
"""

from flask import Flask, request

app = Flask(__name__)


@app.route("/add")
def add():
    a = int(request.args.get("a"))  # pyrefly: ignore[bad-argument-type]
    b = int(request.args.get("b"))  # pyrefly: ignore[bad-argument-type]
    return str(a + b)


app.run(port=8081)
