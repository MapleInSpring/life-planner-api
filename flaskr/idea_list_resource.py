from flask import request
from flask_restful import Resource
from .mind_client import MindClient


class IdeaList(Resource):

    def get(self):
        return MindClient.get_all_ideas()

    def post(self):
        parent = request.json['parent']
        title = request.json['title']

        MindClient.update_idea(parent, title)
