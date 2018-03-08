import json
import requests


def test_scale_get_missing(regtest, db, url):
    r = requests.get(url + '/scale')
    regtest.write(r.text)


def test_scale_get_incorrect(regtest, db, url):
    r = requests.get(url + '/scale/abcd')
    regtest.write(r.text)


def test_scale_get(regtest, db, url):
    r = requests.get(url + '/scale/hashes')
    regtest.write(str(r.json()['data']['scale']['name']))


def test_scales_get_all(regtest, db, url):
    r = requests.get(url + '/scales')
    name = 'none'
    for m in r.json()['data']['scales']:
        if m['name'] == 'hashes':
            name = m['name']
            break
    regtest.write(name)


def test_scales_get_all_file(regtest, db, url):
    data = "?file_type=file"
    r = requests.get(url + '/scales' + data)
    regtest.write(str(len(r.json()['data']['scales'])))


def test_scales_get_all_memory(regtest, db, url):
    data = "?file_type=memory"
    r = requests.get(url + '/scales' + data)
    regtest.write(str(len(r.json()['data']['scales'])))


def test_scales_get_reload(regtest, db, url):
    r = requests.get(url + '/scales?reload=True')
    name = 'none'
    for m in r.json()['data']['scales']:
        if m['name'] == 'hashes':
            name = m['name']
            break
    regtest.write(name)
