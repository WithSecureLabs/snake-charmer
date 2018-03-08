import json
import requests


def test_note_post_missing(regtest, db, url, file_n):
    r = requests.post(url + '/note')
    regtest.write(r.text)


def test_note_post_missing_1(regtest, db, url, file_n):
    data = {
        "body": "abcd",
        "sha256_digest": "abcd"
    }
    r = requests.post(url + '/note', json=data)
    regtest.write(r.text)


def test_note_post(regtest, db, url, file_n):
    data = {
        "body": "abcd",
        "sha256_digest": file_n['sha256_digest']
    }
    r = requests.post(url + '/note', json=data)
    n = r.json()
    n['data']['note']['timestamp'] = None
    regtest.write(str(json.dumps(n, sort_keys=True)))


def test_note_get_missing(regtest, db, url):
    r = requests.get(url + '/note')
    n = r.json()
    regtest.write(str(json.dumps(n, sort_keys=True)))


def test_note_get_missing_1(regtest, db, url):
    r = requests.get(url + '/note/abcd')
    regtest.write(r.text)


def test_note_get(regtest, db, url, file_n):
    r = requests.get(url + '/note/' + file_n['sha256_digest'])
    n = r.json()
    n['data']['note']['timestamp'] = None
    regtest.write(str(json.dumps(n, sort_keys=True)))


def test_note_patch_missing(regtest, db, url):
    r = requests.patch(url + '/note/abcd')
    regtest.write(r.text)


def test_note_patch_missing_1(regtest, db, url, file_n):
    r = requests.patch(url + '/note/' + file_n['sha256_digest'])
    regtest.write(r.text)


def test_note_patch(regtest, db, url, file_n):
    data = '{"body": "abcd"}'
    r = requests.patch(url + '/note/' + file_n['sha256_digest'], data=data)
    n = r.json()
    n['data']['note']['timestamp'] = None
    n['data']['note']['updated_time'] = None
    regtest.write(str(json.dumps(n, sort_keys=True)))


def test_note_put_missing(regtest, db, url):
    r = requests.put(url + '/note/abcd')
    regtest.write(r.text)


def test_note_put_missing_1(regtest, db, url, file_n):
    r = requests.put(url + '/note/' + file_n['sha256_digest'])
    regtest.write(r.text)


def test_note_put(regtest, db, url, file_n):
    data = '{"body": "abcd"}'
    r = requests.put(url + '/note/' + file_n['sha256_digest'], data=data)
    n = r.json()
    n['data']['note']['timestamp'] = None
    n['data']['note']['updated_time'] = None
    regtest.write(str(json.dumps(n, sort_keys=True)))


def test_note_delete_missing(regtest, db, url):
    r = requests.delete(url + '/note/abcd')
    regtest.write(r.text)


def test_note_delete(regtest, db, url, file_n):
    r = requests.delete(url + '/note/' + file_n['sha256_digest'])
    regtest.write(str(r.status_code))


def test_notes_post_missing(regtest, db, url, file_n):
    r = requests.post(url + '/notes')
    regtest.write(r.text)


def test_notes_post_missing_1(regtest, db, url, file_n, memory_n):
    data = [
        {
            "body": "abcd",
            "sha256_digest": "abcd"
        },
        {
            "body": "abcd",
            "sha256_digest": "abcd"
        },
    ]
    r = requests.post(url + '/notes', json=data)
    regtest.write(r.text)


def test_notes_post(regtest, db, url, file_n, memory_n):
    data = [
        {
            "body": "abcd",
            "sha256_digest": file_n['sha256_digest']
        },
        {
            "body": "abcd",
            "sha256_digest": memory_n['sha256_digest']
        },
    ]
    r = requests.post(url + '/notes', json=data)
    n = r.json()
    n['data']['notes'][0]['timestamp'] = None
    n['data']['notes'][1]['timestamp'] = None
    regtest.write(str(json.dumps(n, sort_keys=True)))


def test_notes_get_all(regtest, db, url, file_n):
    r = requests.get(url + '/notes')
    n = r.json()
    n['data']['notes'][0]['timestamp'] = None
    n['data']['notes'][0]['updated_time'] = None
    n['data']['notes'][1]['timestamp'] = None
    n['data']['notes'][1]['updated_time'] = None
    regtest.write(str(json.dumps(n, sort_keys=True)))


def test_notes_get_one(regtest, db, url, file_n):
    r = requests.get(url + '/notes?sha256_digest=' + file_n['sha256_digest'])
    n = r.json()
    n['data']['notes'][0]['timestamp'] = None
    n['data']['notes'][0]['updated_time'] = None
    regtest.write(str(json.dumps(n, sort_keys=True)))


def test_notes_get_missing(regtest, db, url, file_n):
    r = requests.get(url + '/notes?sha256_digest=abcd')
    regtest.write(r.text)
