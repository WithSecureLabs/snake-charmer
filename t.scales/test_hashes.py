import json
import requests


def test_hashes_scale(regtest, db, url):
    r = requests.get(url + '/scale/hashes')
    m = r.json()['data']['scale']
    regtest.write(str(json.dumps(m, sort_keys=True)))


def test_hashes_md5_file(regtest, db, url, file):
    data = {
        "sha256_digest": file['sha256_digest'],
        "scale": "hashes",
        "command": "md5_digest"
    }
    r = requests.post(url + '/command', json=data)
    cmd = r.json()
    cmd['data']['command']['timestamp'] = None
    cmd['data']['command']['start_time'] = None
    cmd['data']['command']['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_hashes_sha1_file(regtest, db, url, file):
    data = {
        "sha256_digest": file['sha256_digest'],
        "scale": "hashes",
        "command": "sha1_digest"
    }
    r = requests.post(url + '/command', json=data)
    cmd = r.json()
    cmd['data']['command']['timestamp'] = None
    cmd['data']['command']['start_time'] = None
    cmd['data']['command']['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_hashes_sha512_file(regtest, db, url, file):
    data = {
        "sha256_digest": file['sha256_digest'],
        "scale": "hashes",
        "command": "sha512_digest"
    }
    r = requests.post(url + '/command', json=data)
    cmd = r.json()
    cmd['data']['command']['timestamp'] = None
    cmd['data']['command']['start_time'] = None
    cmd['data']['command']['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_hashes_md5_mem(regtest, db, url, memory):
    data = {
        "sha256_digest": memory['sha256_digest'],
        "scale": "hashes",
        "command": "md5_digest"
    }
    r = requests.post(url + '/command', json=data)
    cmd = r.json()
    cmd['data']['command']['timestamp'] = None
    cmd['data']['command']['start_time'] = None
    cmd['data']['command']['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_hashes_sha1_mem(regtest, db, url, memory):
    data = {
        "sha256_digest": memory['sha256_digest'],
        "scale": "hashes",
        "command": "sha1_digest"
    }
    r = requests.post(url + '/command', json=data)
    cmd = r.json()
    cmd['data']['command']['timestamp'] = None
    cmd['data']['command']['start_time'] = None
    cmd['data']['command']['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_hashes_sha512_mem(regtest, db, url, memory):
    data = {
        "sha256_digest": memory['sha256_digest'],
        "scale": "hashes",
        "command": "sha512_digest"
    }
    r = requests.post(url + '/command', json=data)
    cmd = r.json()
    cmd['data']['command']['timestamp'] = None
    cmd['data']['command']['start_time'] = None
    cmd['data']['command']['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


# TODO: Test all
# TODO: Fuzzy should be removed
