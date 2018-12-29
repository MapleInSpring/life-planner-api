class TransformerDTO:

    @staticmethod
    def transform_idea_list_dto(idea_list):
        idea_list_dto = []
        for idea in idea_list.copy():
            idea['category'] = idea['category'].name
            idea_list_dto.append(idea)

        return idea_list_dto
