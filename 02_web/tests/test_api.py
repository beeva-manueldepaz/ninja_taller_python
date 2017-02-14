import json
import requests

def test_my_first_test():
    assert 1!=2

def test_api_home():
    r = requests.get("http://127.0.0.1:5000/")
    assert r.content == b"Hello World"

def test_api_json():
    r = requests.get("http://127.0.0.1:5000/hello")
    # assert r.content == json.dumps(dict(message="Hello from python")) # problemas de formato

    r_json = json.loads(r.content.decode())
    value = dict(message="Hello from python")
    assert r_json == value

def test_api_sum_ko():
    r = requests.get("http://127.0.0.1:5000/sum")

    r_json = json.loads(r.content.decode())
    value = dict(sum=0)
    assert r_json == value

def test_api_sum_ok():
    r = requests.get("http://127.0.0.1:5000/sum?num1=2&num2=2")

    r_json = json.loads(r.content.decode())
    value = dict(sum=4)
    assert r_json == value
