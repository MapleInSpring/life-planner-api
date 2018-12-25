from flask import Flask, request
from flask_restful import Resource, Api
from requests_xml import XMLSession
from .mind_auth import MindAuth
from .web_utils import WebUtils
from .transformer import Transformer


app = Flask(__name__)
api = Api(app)
session = XMLSession()


class IdeaList(Resource):
    base_url = 'https://www.mindmeister.com/services/rest?'

    def get(self):
        params = WebUtils.get_default_params()
        params['method'] = 'mm.maps.getMap'
        params['api_sig'] = MindAuth.generate_signing_signature(params)

        get_map_url = self.base_url + WebUtils.generate_param_query_str(params)
        rspJson = WebUtils.get_res_json(session.get(get_map_url))

        return Transformer.transform_idea_list(rspJson)

    def post(self):
        params = WebUtils.get_default_params()
        params['method'] = 'mm.ideas.insert'
        params['parent_id'] = request.json['parent']
        params['title'] = request.json['title']
        params['api_sig'] = MindAuth.generate_signing_signature(params)

        add_ideal_url = self.base_url + WebUtils.generate_param_query_str(params)
        session.get(add_ideal_url)


api.add_resource(IdeaList, '/ideas')

if __name__ == '__main__':
    app.run(port=8080)
