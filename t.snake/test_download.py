import requests


def test_download_get_missing(regtest, db, url):
    r = requests.get(url + '/download')
    regtest.write(r.text)


def test_download_get_incorrect(regtest, db, url):
    r = requests.get(url + '/download/abcd')
    regtest.write(r.text)


def test_download_get(regtest, db, url, file):
    r = requests.get(url + '/download/' + file['sha256_digest'])
    regtest.write(r.text)
