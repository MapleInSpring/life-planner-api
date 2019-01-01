from flask_restful import Resource
from .mind_client import MindClient
from .models.idea_category import IdeaCategory
from .transformer_dto import TransformerDTO


class ActionList(Resource):
    def get(self):
        idea_list = MindClient.get_all_ideas()

        actions = [idea for idea in idea_list if idea['category'] != IdeaCategory.DEFAULT]

        return TransformerDTO.transform_idea_list_dto(actions)
