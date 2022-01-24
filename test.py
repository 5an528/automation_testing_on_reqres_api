# from six.moves import collections_abc

import pytest
import allure
import unittest

class JsonData:

    json_data={
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    json_data_invalid_email={
        "email": "abcd",
        "password": "pistol"
    }

    json_data_empty_password={
        "email": "eve.holt@reqres.in",
        "password": ""
    }

    json_data_invalid_password={
        "email": "eve.holt@reqres.in",
        "password": "rifel"
    }

    login_data={
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    login_data_invalid_email={
        "email": "abc",
        "password": "cityslicka"
    }
    login_data_invalid_password={
        "email": "eve.holt@reqres.in",
        "password": "wrong_pass"
    }
    login_data_empty_email={
        "email": "",
        "password": "cityslicka"
    }


    login_data_empty_password={
        "email": "eve.holt@reqres.in",
        "password": ""
    }

    post_user={
        "name": "morpheus",
        "job": "leader"
    
    }
    post_user_invalid={
        "name": "",
        
    }
    updated_user={
        "name": "morpheus",
        "job": "zion resident"
    }

class Api(JsonData):

    def signup_post(self,url,json_data):
        import requests
        import json
        response=requests.post(url,json_data)
        return response.json()


    def signup_get(self,url,json_data):
        import requests
        import json
        response=requests.get(url,json_data)
        return response.json()
         # print(json.dumps(response.json()))
         # print(response.status_code)

    def login_post(self,url,json_data):
        import requests
        import json
        response=requests.post(url,json_data)
        return response.json()
         # print(json.dumps(response.json()))
         # print(response.status_code)

    def login_get(self,url,json_data):
        import requests
        import json
        response=requests.post(url,json_data)
        return response.json()
         # print(json.dumps(response.json()))
         # print(response.status_code)

    def list_users_get(self,url):
        import requests
        import json
        response=requests.get(url)
        return response.json()
         # print(json.dumps(response.json()))
         # print(response.status_code)

    def single_users_get(self,url):
        import requests
        import json
        response=requests.get(url)
        return response.json()
         # print(json.dumps(response.json()))
         # print(response.status_code)

    def post_user(self,url,json_data):
        import requests
        import json
        response=requests.post(url,json_data)
        return response.json()
         # print(json.dumps(response.json()))
         # print(response.status_code)

    def updated_user(self,url,json_data):
        import requests
        import json
        response=requests.post(url,json_data)
        return response.json()
         # print(json.dumps(response.json()))
         # print(response.status_code)

    def delayed_response(self,url):
        import requests
        import json
        response=requests.get(url)
        return response.json()
         # print(json.dumps(response.json()))
         # print(response.status_code)








        


