import unittest
from test import *
import pytest

api=Api()
data=JsonData()
def test_signup_post():
    outcome=api.signup_post('https://reqres.in/api/register',data.json_data)
    result={"id": 4, "token": "QpwL5tke4Pnpja7X4"}
    if outcome==result:
        assert True
    else:
        assert False

def test_signup_post_empty_password():
    outcome=api.signup_post('https://reqres.in/api/register',data.json_data_empty_password)
    result={"error": "Missing password"}
    if outcome==result:
        assert True
    else:
        assert False

def test_signup_post_invalid_email():
    outcome=api.signup_post('https://reqres.in/api/register',data.json_data_invalid_email)
    result={"error": "Note: Only defined users succeed registration"}
    if outcome==result:
        assert True
    else:
        assert False

def test_signup_post_invalid_password():
    outcome=api.signup_post('https://reqres.in/api/register',data.json_data_invalid_password)
    result={"error": "Missing password"}
    if outcome==result:
        assert True
    else:
        assert False

def test_signup_get():
    outcome=api.signup_get('https://reqres.in/api/register',data.json_data)
    result={"page": 1, "per_page": 6, "total": 12, "total_pages": 2, "data": [{"id": 1, "name": "cerulean", "year": 2000, "color": "#98B2D1", "pantone_value": "15-4020"}, {"id": 2, "name": "fuchsia rose", "year": 2001, "color": "#C74375", "pantone_value": "17-2031"}, {"id": 3, "name": "true red", "year": 2002, "color": "#BF1932", "pantone_value": "19-1664"}, {"id": 4, "name": "aqua sky", "year": 2003, "color": "#7BC4C4", "pantone_value": "14-4811"}, {"id": 5, "name": "tigerlily", "year": 2004, "color": "#E2583E", "pantone_value": "17-1456"}, {"id": 6, "name": "blue turquoise", "year": 2005, "color": "#53B0AE", "pantone_value": "15-5217"}], "support": {"url": "https://reqres.in/#support-heading", "text": "To keep ReqRes free, contributions towards server costs are appreciated!"}}
    if outcome==result:
        assert True
    else:
        assert False
    
def test_login_post():
    outcome=api.login_post('https://reqres.in/api/login',data.login_data)
    result={"token": "QpwL5tke4Pnpja7X4"}
    if outcome==result:
        assert True
    else:
        assert False

def test_login_post_invalid_email():
    outcome=api.login_post('https://reqres.in/api/login',data.login_data_invalid_email)
    result={"error": "user not found"}
    if outcome==result:
        assert True
    else:
        assert False
def test_login_post_invalid_password():
    outcome=api.login_post('https://reqres.in/api/login',data.login_data_invalid_password)
    result={"token": "QpwL5tke4Pnpja7X4"}
    if outcome==result:
        assert True
    else:
        assert False

def test_login_post_empty_email():
    outcome=api.login_post('https://reqres.in/api/login',data.login_data_empty_email)
    result={"error": "Missing email or username"}
    if outcome==result:
        assert True
    else:
        assert False

def test_login_post_empty_password():
    outcome=api.login_post('https://reqres.in/api/login',data.login_data_empty_password)
    result={"error": "Missing password"}
    if outcome==result:
        assert True
    else:
        assert False


def test_login_invalid_url():
    outcome=api.login_post('https://reqres.in/api/login',data.login_data)
    result={}
    if outcome==result:
        assert True
    else:
        assert False


def test_login_get():
    outcome=api.login_get('https://reqres.in/api/login',data.login_data)
    result={"token": "QpwL5tke4Pnpja7X4"}
    if outcome==result:
        assert True
    else:
        assert False
    
def test_list_users_get():
    outcome=api.list_users_get('https://reqres.in/api/users?page=2')
    result={"page": 2, "per_page": 6, "total": 12, "total_pages": 2, "data": [{"id": 7, "email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson", "avatar": "https://reqres.in/img/faces/7-image.jpg"}, {"id": 8, "email": "lindsay.ferguson@reqres.in", "first_name": "Lindsay", "last_name": "Ferguson", "avatar": "https://reqres.in/img/faces/8-image.jpg"}, {"id": 9, "email": "tobias.funke@reqres.in", "first_name": "Tobias", "last_name": "Funke", "avatar": "https://reqres.in/img/faces/9-image.jpg"}, {"id": 10, "email": "byron.fields@reqres.in", "first_name": "Byron", "last_name": "Fields", "avatar": "https://reqres.in/img/faces/10-image.jpg"}, {"id": 11, "email": "george.edwards@reqres.in", "first_name": "George", "last_name": "Edwards", "avatar": "https://reqres.in/img/faces/11-image.jpg"}, {"id": 12, "email": "rachel.howell@reqres.in", "first_name": "Rachel", "last_name": "Howell", "avatar": "https://reqres.in/img/faces/12-image.jpg"}], "support": {"url": "https://reqres.in/#support-heading", "text": "To keep ReqRes free, contributions towards server costs are appreciated!"}}
    if outcome==result:
        assert True
    else:
        assert False

    
    
        
def test_single_users_get():
    outcome=api.single_users_get('https://reqres.in/api/users/2')
    result={"data": {"id": 2, "email": "janet.weaver@reqres.in", "first_name": "Janet", "last_name": "Weaver", "avatar": "https://reqres.in/img/faces/2-image.jpg"}, "support": {"url": "https://reqres.in/#support-heading", "text": "To keep ReqRes free, contributions towards server costs are appreciated!"}}
    if outcome==result:
        assert True
    else:
        assert False

def test_single_users_invalid_url():
    outcome=api.single_users_get('https://reqres.in/api/users/23') # single user invalid
    result={}
    if outcome==result:
        assert True
    else:
        assert False

def test_post_user():
    outcome=api.post_user('https://reqres.in/api/users',data.post_user)
    result={"name": "morpheus", "job": "leader", "id": "529", "createdAt": "2021-11-03T12:10:21.261Z"}
    if outcome==result:
        assert True
    else:
        assert False

def test_post_user_invalid():
    outcome=api.post_user('https://reqres.in/api/users',data.post_user_invalid)
    result={"name": "", "id": "597", "createdAt": "2021-11-03T12:10:22.456Z"}
    if outcome==result:
        assert True
    else:
        assert False


def test_updated_user():
    outcome=api.updated_user('https://reqres.in/api/users/2',data.updated_user)
    result={"name": "morpheus", "job": "zion resident", "id": "327", "createdAt": "2021-11-03T12:10:23.216Z"}
    if outcome==result:
        assert True
    else:
        assert False

def test_delayed_response():
    outcome=api.delayed_response('https://reqres.in/api/users?delay=3')
    result={"page": 1, "per_page": 6, "total": 12, "total_pages": 2, "data": [{"id": 1, "email": "george.bluth@reqres.in", "first_name": "George", "last_name": "Bluth", "avatar": "https://reqres.in/img/faces/1-image.jpg"}, {"id": 2, "email": "janet.weaver@reqres.in", "first_name": "Janet", "last_name": "Weaver", "avatar": "https://reqres.in/img/faces/2-image.jpg"}, {"id": 3, "email": "emma.wong@reqres.in", "first_name": "Emma", "last_name": "Wong", "avatar": "https://reqres.in/img/faces/3-image.jpg"}, {"id": 4, "email": "eve.holt@reqres.in", "first_name": "Eve", "last_name": "Holt", "avatar": "https://reqres.in/img/faces/4-image.jpg"}, {"id": 5, "email": "charles.morris@reqres.in", "first_name": "Charles", "last_name": "Morris", "avatar": "https://reqres.in/img/faces/5-image.jpg"}, {"id": 6, "email": "tracey.ramos@reqres.in", "first_name": "Tracey", "last_name": "Ramos", "avatar": "https://reqres.in/img/faces/6-image.jpg"}], "support": {"url": "https://reqres.in/#support-heading", "text": "To keep ReqRes free, contributions towards server costs are appreciated!"}}
    if outcome==result:
        assert True
    else:
        assert False











