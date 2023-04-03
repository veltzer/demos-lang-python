import flask
app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "<html><body>Hello World!</body></html>"

@app.route("/curse_me")
def hell():
    return "<html><body>Go to hell!</body></html>"


app.run()
