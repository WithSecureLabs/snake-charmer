import json
import requests


def test_memories_get_all(regtest, db, url, memory):
    r = requests.get(url + '/memories')
    f = r.json()
    f['data']['memories'][0]['timestamp'] = None
    regtest.write(str(json.dumps(f, sort_keys=True)))


def test_memories_get_filter(regtest, db, url, memory):
    r = requests.get(url + '/memories?filter[name]=' + memory['name'])
    f = r.json()
    f['data']['memories'][0]['timestamp'] = None
    regtest.write(str(json.dumps(f, sort_keys=True)))


def test_memories_get_filter_1(regtest, db, url):
    r = requests.get(url + '/memories?filter[name]=abcd')
    regtest.write(r.text)


def test_memory_get_missing(regtest, db, url):
    r = requests.get(url + '/memory')
    regtest.write(r.text)


def test_memory_get_missing_1(regtest, db, url):
    r = requests.get(url + '/memory/abcd')
    regtest.write(r.text)


def test_memory_get(regtest, db, url, memory):
    r = requests.get(url + '/memory/' + memory['sha256_digest'])
    f = r.json()
    f['data']['memory']['timestamp'] = None
    regtest.write(str(json.dumps(f, sort_keys=True)))


def test_memory_patch_missing(regtest, db, url):
    r = requests.patch(url + '/memory/abcd')
    regtest.write(r.text)


def test_memory_patch_missing_1(regtest, db, url, memory):
    r = requests.patch(url + '/memory/' + memory['sha256_digest'])
    regtest.write(r.text)


def test_memory_patch(regtest, db, url, memory):
    data = '{"description": "abcd"}'
    r = requests.patch(url + '/memory/' + memory['sha256_digest'], data=data)
    f = r.json()
    f['data']['memory']['timestamp'] = None
    regtest.write(str(json.dumps(f, sort_keys=True)))


def test_memory_put_missing(regtest, db, url):
    r = requests.put(url + '/memory/abcd')
    regtest.write(r.text)


def test_memory_put_missing_1(regtest, db, url, memory):
    r = requests.put(url + '/memory/' + memory['sha256_digest'])
    regtest.write(r.text)


def test_memory_put(regtest, db, url, memory):
    data = '{"name": "abcd"}'
    r = requests.put(url + '/memory/' + memory['sha256_digest'], data=data)
    f = r.json()
    f['data']['memory']['timestamp'] = None
    regtest.write(str(json.dumps(f, sort_keys=True)))


def test_memory_delete_missing(regtest, db, url):
    r = requests.delete(url + '/memory/abcd')
    regtest.write(r.text)


def test_memory_delete(regtest, db, url, memory):
    r = requests.delete(url + '/memory/' + memory['sha256_digest'])
    regtest.write(str(r.status_code))
