from .web_utils import WebUtils
from .transformer import Transformer
from .mind_auth import MindAuth
from requests_xml import XMLSession

session = XMLSession()


class MindClient:
    base_url = 'https://www.mindmeister.com/services/rest?'

    @staticmethod
    def get_all_ideas():
        params = WebUtils.get_default_params()
        params['method'] = 'mm.maps.getMap'
        params['api_sig'] = MindAuth.generate_signing_signature(params)

        get_map_url = MindClient.base_url + WebUtils.generate_param_query_str(params)
        rspJson = WebUtils.get_res_json(session.get(get_map_url))

        return Transformer.transform_idea_list(rspJson)

    @staticmethod
    def update_idea(parent, title):
        params = WebUtils.get_default_params()
        params['method'] = 'mm.ideas.insert'
        params['parent_id'] = parent
        params['title'] = title
        params['api_sig'] = MindAuth.generate_signing_signature(params)

        add_ideal_url = MindClient.base_url + WebUtils.generate_param_query_str(params)
        print(add_ideal_url)
        session.get(add_ideal_url)
