from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello, World!"}


api.add_resource(HelloWorld, "/")


if __name__ == "__main__":
    app.run(debug=True)
