import json
import requests


def test_upload_file_post_missing(regtest, db, url):
    r = requests.post(url + '/upload')
    regtest.write(r.text)


def test_upload_file_post_missing_1(regtest, db, url):
    r = requests.post(url + '/upload/file')
    regtest.write(r.text)


def test_upload_file_post(regtest, db, url):
    files = {'file': open('files/hello.txt', 'rb')}
    data = {'name': 'file'}
    r = requests.post(url + '/upload/file', files=files, data=data)
    f = r.json()
    f['data']['sample']['timestamp'] = None
    regtest.write(str(json.dumps(f, sort_keys=True)))


def test_upload_file_post_zipped(regtest, db, url):
    files = {'file': open('files/hello_2.zip', 'rb')}
    data = {'name': 'file', 'extract': 'true'}
    r = requests.post(url + '/upload/file', files=files, data=data)
    f = r.json()
    f['data']['sample']['timestamp'] = None
    regtest.write(str(json.dumps(f, sort_keys=True)))


def test_upload_file_post_zipped_password(regtest, db, url):
    files = {'file': open('files/hello_3.zip', 'rb')}
    data = {'name': 'file', 'extract': 'true', 'password': 'password'}
    r = requests.post(url + '/upload/file', files=files, data=data)
    f = r.json()
    f['data']['sample']['timestamp'] = None
    regtest.write(str(json.dumps(f, sort_keys=True)))


def test_upload_file_post_zipped_password_incorrect(regtest, db, url):
    files = {'file': open('files/hello_3.zip', 'rb')}
    data = {'name': 'file', 'extract': 'true', 'password': 'abcd'}
    r = requests.post(url + '/upload/file', files=files, data=data)
    regtest.write(r.text)


def test_upload_file_post_exist(regtest, db, url):
    files = {'file': open('files/hello.txt', 'rb')}
    data = {'name': 'file'}
    r = requests.post(url + '/upload/file', files=files, data=data)
    f = r.json()
    f['data']['sample']['timestamp'] = None
    regtest.write(str(json.dumps(f, sort_keys=True)))


def test_upload_files_post_missing(regtest, db, url):
    r = requests.post(url + '/upload')
    regtest.write(r.text)


def test_upload_files_post_missing_1(regtest, db, url):
    r = requests.post(url + '/upload/files')
    regtest.write(r.text)


def test_upload_files_post_missing_2(regtest, db, url):
    files = {'files[]': open('files/hello.txt', 'rb')}
    r = requests.post(url + '/upload/files', files=files)
    regtest.write(r.text)


def test_upload_files_post_unsupported(regtest, db, url):
    files = {'files[]': open('files/hello.txt', 'rb')}
    data = {'name': 'file'}
    r = requests.post(url + '/upload/files', files=files, json=data)
    regtest.write(r.text)


# TODO: Broken
'''
def test_upload_files_post(regtest, db, url, file):
    requests.delete(url + '/file/' + file['sha256_digest'])
    files = {'files[]': open('files/hello.txt', 'rb')}
    data = {"data": [{"name": "file"}]}
    r = requests.post(url + '/upload/files', files=files, data=data)
    f = r.json()['data']['files']
    f['timestamp'] = None
    regtest.write(str(f))


def test_upload_files_post_exist(regtest, db, url):
    files = {'files[]': open('files/hello.txt', 'rb')}
    data = {"data": [{"name": "file"}]}
    r = requests.post(url + '/upload/files', files=files, data=data)
    f = r.json()['data']['files']
    f['timestamp'] = None
    regtest.write(str(f))
'''


def test_upload_memory_post_missing(regtest, db, url):
    r = requests.post(url + '/upload')
    regtest.write(r.text)


def test_upload_memory_post_missing_1(regtest, db, url):
    r = requests.post(url + '/upload/memory')
    regtest.write(r.text)


def test_upload_memory_post(regtest, db, url):
    files = {'file': open('files/bye.txt', 'rb')}
    data = {'name': 'mem'}
    r = requests.post(url + '/upload/memory', files=files, data=data)
    f = r.json()
    f['data']['sample']['timestamp'] = None
    regtest.write(str(json.dumps(f, sort_keys=True)))


def test_upload_memory_post_exist(regtest, db, url):
    files = {'file': open('files/bye.txt', 'rb')}
    data = {'name': 'mem'}
    r = requests.post(url + '/upload/memory', files=files, data=data)
    f = r.json()
    f['data']['sample']['timestamp'] = None
    regtest.write(str(json.dumps(f, sort_keys=True)))
