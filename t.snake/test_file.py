import json
import requests


def test_files_get_all(regtest, db, url, file):
    r = requests.get(url + '/files')
    f = r.json()
    f['data']['files'][0]['timestamp'] = None
    regtest.write(str(json.dumps(f, sort_keys=True)))


def test_files_get_filter(regtest, db, url, file):
    r = requests.get(url + '/files?filter[name]=' + file['name'])
    f = r.json()
    f['data']['files'][0]['timestamp'] = None
    regtest.write(str(json.dumps(f, sort_keys=True)))


def test_files_get_filter_1(regtest, db, url):
    r = requests.get(url + '/files?filter[name]=abcd')
    regtest.write(r.text)


def test_file_hex_get_missing(regtest, db, url):
    r = requests.get(url + '/file/abcd/hex')
    regtest.write(r.text)


def test_file_hex_get(regtest, db, url, file):
    r = requests.get(url + '/file/' + file['sha256_digest'] + '/hex')
    regtest.write(r.text)


def test_file_get_missing(regtest, db, url):
    r = requests.get(url + '/file')
    regtest.write(r.text)


def test_file_get_missing_1(regtest, db, url):
    r = requests.get(url + '/file/abcd')
    regtest.write(r.text)


def test_file_get(regtest, db, url, file):
    r = requests.get(url + '/file/' + file['sha256_digest'])
    f = r.json()
    f['data']['file']['timestamp'] = None
    regtest.write(str(json.dumps(f, sort_keys=True)))


def test_file_patch_missing(regtest, db, url):
    r = requests.patch(url + '/file/abcd')
    regtest.write(r.text)


def test_file_patch_missing_1(regtest, db, url, file):
    r = requests.patch(url + '/file/' + file['sha256_digest'])
    regtest.write(r.text)


def test_file_patch(regtest, db, url, file):
    data = '{"description": "abcd"}'
    r = requests.patch(url + '/file/' + file['sha256_digest'], data=data)
    f = r.json()
    f['data']['file']['timestamp'] = None
    regtest.write(str(json.dumps(f, sort_keys=True)))


def test_file_put_missing(regtest, db, url):
    r = requests.put(url + '/file/abcd')
    regtest.write(r.text)


def test_file_put_missing_1(regtest, db, url, file):
    r = requests.put(url + '/file/' + file['sha256_digest'])
    regtest.write(r.text)


def test_file_put(regtest, db, url, file):
    data = '{"name": "abcd"}'
    r = requests.put(url + '/file/' + file['sha256_digest'], data=data)
    f = r.json()
    f['data']['file']['timestamp'] = None
    regtest.write(str(json.dumps(f, sort_keys=True)))


def test_file_delete_missing(regtest, db, url):
    r = requests.delete(url + '/file/abcd')
    regtest.write(r.text)


def test_file_delete(regtest, db, url, file):
    r = requests.delete(url + '/file/' + file['sha256_digest'])
    regtest.write(str(r.text))
    regtest.write(str(r.status_code))
