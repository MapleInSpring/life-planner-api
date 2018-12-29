from flask import request
from flask_restful import Resource
from .mind_client import MindClient
from .transformer_dto import TransformerDTO


class IdeaList(Resource):

    def get(self):
        idea_list = MindClient.get_all_ideas()

        return TransformerDTO.transform_idea_list_dto(idea_list)

    def post(self):
        parent = request.json['parent']
        title = request.json['title']

        MindClient.update_idea(parent, title)
