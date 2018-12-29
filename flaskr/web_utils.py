from requests_xml import XML
import json


class WebUtils:
    knowledge_map_id = 1193541820
    action_map_id = 1195047869

    @staticmethod
    def generate_param_query_str(params):
        param_key_values = []
        for key, value in params.items():
            param_key_values.append('{}={}'.format(key, value))

        return '&'.join(param_key_values)

    @staticmethod
    def get_default_params():
        params = {}
        params["api_key"] = 'da85a513e81709500df4387d1fb2c9bf'
        params["auth_token"] = 'ZAj1q3RiBlr3Xy7CwaIU'
        params["response_format"] = 'xml'
        params["map_id"] = WebUtils.knowledge_map_id

        return params

    @staticmethod
    def get_res_json(response):
        rsp = response.xml.xpath('//rsp', first=True)
        return json.loads(XML(xml=rsp.xml).json())['rsp']
