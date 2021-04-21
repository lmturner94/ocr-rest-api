from flask import Flask
from flask_restful import Api

from todo import Todo

app = Flask(__name__)
api = Api(app)
server = app.server
api.add_resource(Todo, "/todo/<int:id>")


if __name__ == "__main__":
  app.run()

  