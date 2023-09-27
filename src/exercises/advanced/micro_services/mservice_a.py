from flask import Flask
from flask import request
import requests

app = Flask(__name__)

HTML = """
<html>
<body>
<form action="/add" method="get">
<label for="a">A:</label>
<input type="text" id="a" name="a"></input><br><br>
<label for="b">B:</label>
<input type="text" id="b" name="b"></input><br><br>
<input type="submit" value="Do the hard calculation">
</form>
</body>
</html>
"""

@app.route("/")
def form():
    return HTML

@app.route("/add")
def add():
    # curl "http://localhost:8081/add?a=X&b=Y"
    response = requests.get(
            url=f"http://localhost:8081/add",
            params=request.args,
            timeout=5,
    )
    response.raise_for_status()
    return f"the result is {response.text}"


app.run(port=8080)
