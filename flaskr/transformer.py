class Transformer:

    @staticmethod
    def transform_idea_list(res_json):
        return [Transformer.transform_idea(idea) for idea in res_json['ideas']['idea']]

    @staticmethod
    def transform_idea(idea):
        return {
            'id': idea['id']['$'],
            'title': idea['title']['$'],
            'parent': idea['parent']['$'] if idea['parent'] else -1
        }
