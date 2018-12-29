from flask import Flask
from flask_restful import Api
from .idea_list_resource import IdeaList
from .action_list_resource import ActionList


app = Flask(__name__)
api = Api(app)


api.add_resource(IdeaList, '/ideas')
api.add_resource(ActionList, '/actions')

if __name__ == '__main__':
    app.run(port=8080)
