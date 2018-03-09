import requests


def test_store_get(regtest, db, url, file, memory):
    r = requests.get(url + '/store')
    regtest.write(str(len(r.json()['data']['samples'])))


def test_store_file(regtest, db, url, file, memory):
    data = "?file_type=file"
    r = requests.get(url + '/store' + data)
    regtest.write(str(len(r.json()['data']['samples'])))


def test_store_memory(regtest, db, url, file, memory):
    data = "?file_type=memory"
    r = requests.get(url + '/store' + data)
    regtest.write(str(len(r.json()['data']['samples'])))


def test_store_filter(regtest, db, url, file, memory):
    data = "?filter[name]=" + file['name']
    r = requests.get(url + '/store' + data)
    regtest.write(str(len(r.json()['data']['samples'])))


def test_store_filter_and(regtest, db, url, file, memory):
    data = "?filter[name]=" + file['name'] + \
           "&filter[name]=" + memory['name']
    r = requests.get(url + '/store' + data)
    regtest.write(str(len(r.json()['data']['samples'])))


def test_store_filter_and_1(regtest, db, url, file, memory):
    data = "?filter[name]=" + file['name'] + \
           "&filter[file_type]=" + file['file_type']
    r = requests.get(url + '/store' + data)
    regtest.write(str(len(r.json()['data']['samples'])))


def test_store_filter_or(regtest, db, url, file, memory):
    data = "?filter[name]=" + file['name'] + \
           "&filter[name]=" + memory['name'] + \
           "&operator=or"
    r = requests.get(url + '/store' + data)
    regtest.write(str(len(r.json()['data']['samples'])))


def test_store_limit(regtest, db, url, file, memory):
    data = "?limit=1"
    r = requests.get(url + '/store' + data)
    regtest.write(str(len(r.json()['data']['samples'])))
