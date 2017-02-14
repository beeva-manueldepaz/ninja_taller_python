import json
import requests

def test_my_first_test():
    assert 1!=2

def test_api_home():
    r = requests.get("http://127.0.0.1:5000/")
    assert r.content == b"Hello World"

def test_api_json():
    r = requests.get("http://127.0.0.1:5000/hello")
    assert r.content == json.dumps(dict(message="Hello from python"))
