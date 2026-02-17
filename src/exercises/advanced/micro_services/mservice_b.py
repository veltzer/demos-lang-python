"""
mservice_b.py
"""

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/add")
def add():
    a = int(request.args.get("a"))  # pyrefly: ignore[no-matching-overload]
    b = int(request.args.get("b"))  # pyrefly: ignore[no-matching-overload]
    return str(a + b)


app.run(port=8081)
