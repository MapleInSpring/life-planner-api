from flask import Flask, request
from flask_restful import Resource, Api
from requests_xml import XMLSession, XML
import json
import hashlib

app = Flask(__name__)
api = Api(app)
session = XMLSession()


class IdeaList(Resource):
    def get(self):
        r = session.get('https://www.mindmeister.com/services/rest?api_key=da85a513e81709500df4387d1fb2c9bf&auth_token=ZAj1q3RiBlr3Xy7CwaIU&map_id=1193541820&method=mm.maps.getMap&response_format=xml&api_sig=b9fd158ee1e9200074710c87dbbb0cf1')
        rsp = r.xml.xpath('//rsp', first=True)
        rspJson = json.loads(XML(xml=rsp.xml).json())['rsp']

        map_ideas = {}
        map_ideas['mapId'] = rspJson['map']['@id']
        map_ideas['ideas'] = [self.transform_idea(idea) for idea in rspJson['ideas']['idea']]

        return map_ideas

    def post(self):
        params = {}
        params["api_key"] = 'da85a513e81709500df4387d1fb2c9bf'
        params["auth_token"] = 'ZAj1q3RiBlr3Xy7CwaIU'
        params["response_format"] = 'xml'
        params["method"] = 'mm.ideas.insert'
        params["map_id"] = 1193541820
        params["parent_id"] = request.json['parent']
        params["title"] = request.json['title']
        params["api_sig"] = self.generate_signing_signature(params)

        add_ideal_url = 'https://www.mindmeister.com/services/rest?' + self.generate_param_query_str(params)
        print(add_ideal_url)
        session.get(add_ideal_url)

    def transform_idea(self, idea):
        concise_idea = {
            'id': idea['id']['$'],
            'title': idea['title']['$'],
            'parent': idea['parent']['$'] if idea['parent'] else -1
        }
        return concise_idea

    def generate_signing_signature(self, params):
        secret_key = '2292dcc3fd240176'
        param_key_values = []
        for key, value in params.items():
            param_key_values.append('{}{}'.format(key, value))

        param_key_values.sort()
        param_joint_string = ''.join(param_key_values)
        md5_encode_string = hashlib.md5(str(secret_key + param_joint_string).encode('utf-8'))
        return md5_encode_string.hexdigest()

    def generate_param_query_str(self, params):
        param_key_values = []
        for key, value in params.items():
            param_key_values.append('{}={}'.format(key, value))

        return '&'.join(param_key_values)

api.add_resource(IdeaList, '/ideas')

if __name__ == '__main__':
    app.run(port=8080)
