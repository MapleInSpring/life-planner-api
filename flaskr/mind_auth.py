import hashlib


class MindAuth:

    @staticmethod
    def generate_signing_signature(params):
        secret_key = '2292dcc3fd240176'
        param_key_values = []
        for key, value in params.items():
            param_key_values.append('{}{}'.format(key, value))

        param_key_values.sort()
        param_joint_string = ''.join(param_key_values)
        md5_encode_string = hashlib.md5(str(secret_key + param_joint_string).encode('utf-8'))

        return md5_encode_string.hexdigest()
