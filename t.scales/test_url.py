import json
import requests


def test_url_scale(regtest, db, url):
    r = requests.get(url + '/scale/url')
    m = r.json()['data']['scale']
    regtest.write(str(json.dumps(m, sort_keys=True)))


def test_url_upload(regtest, db, url, file):
    data = {
        "args": {
            "url":'http://127.0.0.1:6000/api',
        }
    }
    r = requests.post(url + '/scale/url/upload', json=data)
    cmd = r.json()
    cmd['data']['sample']['timestamp'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))
