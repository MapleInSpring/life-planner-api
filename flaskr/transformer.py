class Transformer:

    @staticmethod
    def transform_idea_list(res_json):
        map_ideas = {}
        map_ideas['mapId'] = res_json['map']['@id']
        map_ideas['ideas'] = [Transformer.transform_idea(idea) for idea in res_json['ideas']['idea']]

        return map_ideas

    @staticmethod
    def transform_idea(idea):
        return {
            'id': idea['id']['$'],
            'title': idea['title']['$'],
            'parent': idea['parent']['$'] if idea['parent'] else -1
        }
