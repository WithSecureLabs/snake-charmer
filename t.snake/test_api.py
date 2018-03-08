import requests


def test_api_route(regtest, db, url):
    r = requests.get(url + '/api')
    regtest.write(r.text)
