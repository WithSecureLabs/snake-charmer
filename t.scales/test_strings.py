import json
import requests


def test_strings_scale(regtest, db, url):
    r = requests.get(url + '/scale/strings')
    m = r.json()['data']['scale']
    regtest.write(str(json.dumps(m, sort_keys=True)))


def test_strings_all_strings(regtest, db, url, file):
    data = {
        "sha256_digest": file['sha256_digest'],
        "scale": "strings",
        "command": "all_strings"
    }
    r = requests.post(url + '/command', json=data)
    cmd = r.json()
    cmd['data']['command']['timestamp'] = None
    cmd['data']['command']['start_time'] = None
    cmd['data']['command']['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_strings_interesting(regtest, db, url, file):
    data = {
        "sha256_digest": file['sha256_digest'],
        "scale": "strings",
        "command": "interesting"
    }
    r = requests.post(url + '/command', json=data)
    cmd = r.json()
    cmd['data']['command']['timestamp'] = None
    cmd['data']['command']['start_time'] = None
    cmd['data']['command']['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))
