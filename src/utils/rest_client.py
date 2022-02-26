import requests
import json

class RestClient:
    
    def __init__(self):
        self._headers = {}

    def with_header(self, key, val):
        self._headers[key] = val
        return self

    def with_token(self, token):
        self._headers['Authorization'] = 'Token ' + token
        return self

    def get(self, url, params={}):
        self._res = requests.get(url, headers=self._headers, params=params)
        return self

    def post(self, url, params={}):
        self._res = requests.post(url,headers=self._headers, params=params)
        return self

    def put(self, url, params={}):
        self._res = requests.put(url, headers=self._headers, params=params)
        return self

    def delete(self, url, params={}):
        self._res = requests.delete(url, headers=self._headers, params=params)
        return self
     
    def get_response(self):
        return self._res

    def is_status_ok(self):
        return self._res.status_code == requests.codes.ok

    def get_response_json(self):
        return self._res.json()

    def pretty_print(self):
        req = self._res.request
        print('{}\n{}\r\n{}\r\n\r\n{}'.format('-----------START-----------',req.method + ' ' + req.url,'\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),req.body))
