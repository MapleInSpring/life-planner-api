from .models.idea_category import IdeaCategory


class TransformerDomain:

    @staticmethod
    def transform_idea_list(res_json):
        return [TransformerDomain.transform_idea(idea) for idea in res_json['ideas']['idea']]

    @staticmethod
    def transform_idea(idea):
        idea_icon = idea['icon']['$'] if idea['icon'] else ''
        return {
            'id': idea['id']['$'],
            'title': idea['title']['$'],
            'parent': idea['parent']['$'] if idea['parent'] else -1,
            'category': IdeaCategory(idea_icon)
        }
