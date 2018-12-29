from flask import Flask
from flask_restful import Api
from .idea_list_resource import IdeaList


app = Flask(__name__)
api = Api(app)


api.add_resource(IdeaList, '/ideas')

if __name__ == '__main__':
    app.run(port=8080)
