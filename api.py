from flask import Flask
from flask_restful import Resource, Api
from requests_xml import XMLSession, XML
import json

app = Flask(__name__)
api = Api(app)
session = XMLSession()


class IdeaList(Resource):
    def get(self):
        r = session.get('https://www.mindmeister.com/services/rest?api_key=da85a513e81709500df4387d1fb2c9bf&auth_token=ZAj1q3RiBlr3Xy7CwaIU&map_id=1193541820&method=mm.maps.getMap&response_format=xml&api_sig=b9fd158ee1e9200074710c87dbbb0cf1')
        rsp = r.xml.xpath('//rsp', first=True)
        return json.loads(XML(xml=rsp.xml).json())

api.add_resource(IdeaList, '/ideas')

if __name__ == '__main__':
    app.run(debug=True)
