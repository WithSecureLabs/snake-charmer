import requests
import pytest

from os import environ

URL = environ['SNAKE_API']


@pytest.fixture(scope="module")
def file_n():
    files = {'file': open('files/hello_n.txt', 'rb')}
    data = {'name': 'hello.txt'}
    r = requests.post(URL + '/upload/file', files=files, data=data)
    return r.json()['data']['sample']


@pytest.fixture(scope="module")
def memory_n():
    files = {'file': open('files/bye_n.txt', 'rb')}
    data = {'name': 'bye.txt'}
    r = requests.post(URL + '/upload/memory', files=files, data=data)
    return r.json()['data']['sample']
