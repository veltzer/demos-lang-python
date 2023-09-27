from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/add")
def add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(a+b)


app.run(port=8081)
