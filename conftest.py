import requests
import pymongo
import pytest

from os import environ

URL = environ['SNAKE_API']


@pytest.fixture(scope="module")
def db():
    db = pymongo.MongoClient('localhost', int(environ['MONGO_PORT']))
    yield db.snake
    db.drop_database('snake')


@pytest.fixture(scope="module")
def url():
    return URL


@pytest.fixture(scope="module")
def file():
    files = {'file': open('files/hello.txt', 'rb')}
    data = {'name': 'hello.txt'}
    r = requests.post(URL + '/upload/file', files=files, data=data)
    return r.json()['data']['file']


@pytest.fixture(scope="module")
def memory():
    files = {'file': open('files/bye.txt', 'rb')}
    data = {'name': 'bye.txt'}
    r = requests.post(URL + '/upload/memory', files=files, data=data)
    return r.json()['data']['memory']
