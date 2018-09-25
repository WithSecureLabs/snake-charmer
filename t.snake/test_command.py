"""
Test the Command Route API
"""

import json
import requests


# pylint: disable=invalid-name
# pylint: disable=missing-docstring
# pylint: disable=unused-argument


def test_command_post_missing(regtest, db, url):
    r = requests.post(url + '/command')
    regtest.write(r.text)


def test_command_post_missing_1(regtest, db, url):
    data = {"sha256_digest": "abcd"}
    r = requests.post(url + '/command', data=data)
    regtest.write(r.text)


def test_command_post_missing_2(regtest, db, url):
    data = {
        "sha256_digest": "abcd",
        "scale": "hashes"
    }
    r = requests.post(url + '/command', data=data)
    regtest.write(r.text)


def test_command_post_missing_3(regtest, db, url):
    data = {
        "sha256_digest": "abcd",
        "scale": "hashes",
        "command": "all"
    }
    r = requests.post(url + '/command', data=data)
    regtest.write(r.text)


def test_command_post_unknown(regtest, db, url, file):
    data = {
        "sha256_digest": file['sha256_digest'],
        "scale": "hashes",
        "command": "123456"
    }
    r = requests.post(url + '/command', data=data)
    regtest.write(r.text)


def test_command_post(regtest, db, url, file):
    data = {
        "sha256_digest": file['sha256_digest'],
        "scale": "hashes",
        "command": "all"
    }
    r = requests.post(url + '/command', data=data)
    cmd = r.json()
    cmd['data']['command']['timestamp'] = None
    cmd['data']['command']['start_time'] = None
    cmd['data']['command']['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_command_post_not_supported(regtest, db, url, memory):
    data = {
        "sha256_digest": memory['sha256_digest'],
        "scale": "strings",
        "command": "all_strings"
    }
    r = requests.post(url + '/command', json=data)
    regtest.write(r.text)


def test_command_post_args_empty(regtest, db, url, interesting):
    data = {
        "sha256_digest": interesting['sha256_digest'],
        "scale": "strings",
        "command": "interesting",
        "args": {}
    }
    r = requests.post(url + '/command', json=data)
    cmd = r.json()
    cmd['data']['command']['timestamp'] = None
    cmd['data']['command']['start_time'] = None
    cmd['data']['command']['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_command_post_args_present(regtest, db, url, interesting):
    data = {
        "sha256_digest": interesting['sha256_digest'],
        "scale": "strings",
        "command": "interesting",
        "args": {
            "min_length": "10"
        }
    }
    r = requests.post(url + '/command', json=data)
    cmd = r.json()
    cmd['data']['command']['timestamp'] = None
    cmd['data']['command']['start_time'] = None
    cmd['data']['command']['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_command_get_missing(regtest, db, url):
    r = requests.get(url + '/command')
    regtest.write(r.text)


def test_command_get_missing_1(regtest, db, url):
    data = "?sha256_digest=abcd"
    r = requests.get(url + '/command' + data)
    regtest.write(r.text)


def test_command_get_missing_2(regtest, db, url):
    data = "?sha256_digest=abcd" + \
           "&scale=hashes"
    r = requests.get(url + '/command' + data)
    regtest.write(r.text)


def test_command_get_missing_3(regtest, db, url):
    data = "?sha256_digest=abcd" + \
           "&scale=hashes" + \
           "&command=all"
    r = requests.get(url + '/command' + data)
    regtest.write(r.text)


def test_command_get(regtest, db, url, file):
    data = "?sha256_digest=" + file['sha256_digest'] + \
           "&scale=" + "hashes" + \
           "&command=" + "all"
    r = requests.get(url + '/command' + data)
    cmd = r.json()
    cmd['data']['command']['timestamp'] = None
    cmd['data']['command']['start_time'] = None
    cmd['data']['command']['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_command_get_markdown(regtest, db, url, file):
    data = "?sha256_digest=" + file['sha256_digest'] + \
           "&scale=" + "hashes" + \
           "&command=" + "all" + \
           "&format=" + "markdown"
    r = requests.get(url + '/command' + data)
    cmd = r.json()
    cmd['data']['command']['timestamp'] = None
    cmd['data']['command']['start_time'] = None
    cmd['data']['command']['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_command_get_plaintext(regtest, db, url, file):
    data = {
        "sha256_digest": file['sha256_digest'],
        "scale": "strings",
        "command": "all_strings"
    }
    r = requests.post(url + '/command', data=data)
    data = "?sha256_digest=" + file['sha256_digest'] + \
           "&scale=" + "strings" + \
           "&command=" + "all_strings" + \
           "&format=" + "plaintext"
    r = requests.get(url + '/command' + data)
    cmd = r.json()
    cmd['data']['command']['timestamp'] = None
    cmd['data']['command']['start_time'] = None
    cmd['data']['command']['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_command_get_incorrect_format(regtest, db, url, file):
    data = "?sha256_digest=" + file['sha256_digest'] + \
           "&scale=" + "hashes" + \
           "&command=" + "all" + \
           "&format=" + "abcd"
    r = requests.get(url + '/command' + data)
    regtest.write(r.text)


def test_command_get_args_present(regtest, db, url, interesting):
    data = "?sha256_digest=" + interesting['sha256_digest'] + \
           "&scale=" + "strings" + \
           "&command=" + "interesting" + \
           "&format=" + "json" + \
           "&args[min_length]=10"
    r = requests.get(url + '/command' + data)
    cmd = r.json()
    cmd['data']['command']['timestamp'] = None
    cmd['data']['command']['start_time'] = None
    cmd['data']['command']['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_commands_post_missing(regtest, db, url):
    r = requests.post(url + '/commands')
    regtest.write(r.text)


def test_commands_post_missing_1(regtest, db, url):
    r = requests.post(url + '/commands', data={})
    regtest.write(r.text)


def test_commands_post_missing_2(regtest, db, url):
    data = [{"sha256_digests": ["abcd"]}]
    r = requests.post(url + '/commands', json=data)
    regtest.write(r.text)


def test_commands_post_missing_3(regtest, db, url):
    data = [{
        "sha256_digests": ["abcd"],
        "scale": "hashes"
    }]
    r = requests.post(url + '/commands', json=data)
    regtest.write(r.text)


def test_commands_post_missing_4(regtest, db, url):
    data = [{
        "sha256_digests": ["abcd"],
        "scale": "hashes",
        "command": "all"
    }]
    r = requests.post(url + '/commands', json=data)
    regtest.write(r.text)


def test_commands_post(regtest, db, url, file):
    data = [{
        "sha256_digests": [file['sha256_digest']],
        "scale": "hashes",
        "command": "all"
    }]
    r = requests.post(url + '/commands', json=data)
    cmd = r.json()
    cmd['data']['commands'][0]['timestamp'] = None
    cmd['data']['commands'][0]['start_time'] = None
    cmd['data']['commands'][0]['end_time'] = None
    cmd['data']['commands'][0]['status'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_commands_post_all(regtest, db, url):
    data = [{
        "sha256_digests": ['all'],
        "scale": "hashes",
        "command": "all"
    }]
    r = requests.post(url + '/commands', json=data)
    regtest.write(str(len(r.json()['data']['commands'])))


def test_commands_post_all_file(regtest, db, url):
    data = [{
        "sha256_digests": ['all:file'],
        "scale": "hashes",
        "command": "all"
    }]
    r = requests.post(url + '/commands', json=data)
    cmd = r.json()
    cmd['data']['commands'][0]['timestamp'] = None
    cmd['data']['commands'][0]['start_time'] = None
    cmd['data']['commands'][0]['end_time'] = None
    cmd['data']['commands'][0]['status'] = None
    cmd['data']['commands'][1]['timestamp'] = None
    cmd['data']['commands'][1]['start_time'] = None
    cmd['data']['commands'][1]['end_time'] = None
    cmd['data']['commands'][1]['status'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_commands_post_all_file_incorrect(regtest, db, url):
    data = [{
        "sha256_digests": ['all:files'],
        "scale": "hashes",
        "command": "all"
    }]
    r = requests.post(url + '/commands', json=data)
    regtest.write(r.text)


def test_commands_post_not_supported(regtest, db, url, memory):
    data = [{
        "sha256_digests": [memory['sha256_digest']],
        "scale": "strings",
        "command": "all_strings"
    }]
    r = requests.post(url + '/commands', json=data)
    regtest.write(r.text)


def test_commands_post_args_empty(regtest, db, url, interesting):
    data = [{
        "sha256_digests": [interesting['sha256_digest']],
        "scale": "strings",
        "command": "interesting",
        "args": {}
    }]
    r = requests.post(url + '/commands', json=data)
    cmd = r.json()
    cmd['data']['commands'][0]['timestamp'] = None
    cmd['data']['commands'][0]['start_time'] = None
    cmd['data']['commands'][0]['end_time'] = None
    cmd['data']['commands'][0]['status'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_commands_post_args_present(regtest, db, url, interesting):
    data = [{
        "sha256_digests": [interesting['sha256_digest']],
        "scale": "strings",
        "command": "interesting",
        "args": {
            "min_length": 10
        }
    }]
    r = requests.post(url + '/commands', json=data)
    cmd = r.json()
    cmd['data']['commands'][0]['timestamp'] = None
    cmd['data']['commands'][0]['start_time'] = None
    cmd['data']['commands'][0]['end_time'] = None
    cmd['data']['commands'][0]['status'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_commands_get(regtest, db, url, file):
    data = [{
        "sha256_digests": [file['sha256_digest']],
        "scale": "hashes",
        "command": "all"
    }]
    r = requests.get(url + '/commands', json=data)
    cmd = r.json()
    while cmd['data']['commands'][0]['status'] == 'pending' or \
            cmd['data']['commands'][0]['status'] == 'running':
        r = requests.get(url + '/commands', json=data)
        cmd = r.json()
    cmd['data']['commands'][0]['timestamp'] = None
    cmd['data']['commands'][0]['start_time'] = None
    cmd['data']['commands'][0]['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_commands_get_all(regtest, db, url):
    r = requests.get(url + '/commands')
    regtest.write(str(len(r.json()['data']['commands'])))


def test_commands_get_all_file(regtest, db, url):
    data = "?sha256_digest=all:file"
    r = requests.get(url + '/commands' + data)
    regtest.write(str(len(r.json()['data']['commands'])))


def test_commands_get_hash(regtest, db, url, file):
    data = "?sha256_digest=" + file['sha256_digest']
    r = requests.get(url + '/commands' + data)
    cmd = r.json()
    while cmd['data']['commands'][0]['status'] == 'pending' or \
            cmd['data']['commands'][0]['status'] == 'running':
        r = requests.get(url + '/commands' + data)
        cmd = r.json()
    cmd['data']['commands'][0]['timestamp'] = None
    cmd['data']['commands'][0]['start_time'] = None
    cmd['data']['commands'][0]['end_time'] = None
    cmd['data']['commands'][1]['timestamp'] = None
    cmd['data']['commands'][1]['start_time'] = None
    cmd['data']['commands'][1]['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_commands_get_scale(regtest, db, url, file):
    data = "?sha256_digest=" + file['sha256_digest'] + \
           "&scale=hashes"
    r = requests.get(url + '/commands' + data)
    cmd = r.json()
    while cmd['data']['commands'][0]['status'] == 'pending' or \
            cmd['data']['commands'][0]['status'] == 'running':
        r = requests.get(url + '/commands' + data)
        cmd = r.json()
    cmd['data']['commands'][0]['timestamp'] = None
    cmd['data']['commands'][0]['start_time'] = None
    cmd['data']['commands'][0]['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_commands_get_command(regtest, db, url, file):
    data = "?sha256_digest=" + file['sha256_digest'] + \
           "&scale=hashes" + \
           "&command=all"
    r = requests.get(url + '/commands' + data)
    cmd = r.json()
    while cmd['data']['commands'][0]['status'] == 'pending' or \
            cmd['data']['commands'][0]['status'] == 'running':
        r = requests.get(url + '/commands' + data)
        cmd = r.json()
    cmd['data']['commands'][0]['timestamp'] = None
    cmd['data']['commands'][0]['start_time'] = None
    cmd['data']['commands'][0]['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_commands_get_json(regtest, db, url, file):
    data = [{
        "sha256_digests": [file['sha256_digest']],
        "scale": "hashes",
        "command": "all"
    }]
    r = requests.get(url + '/commands', json=data)
    cmd = r.json()
    while cmd['data']['commands'][0]['status'] == 'pending' or \
            cmd['data']['commands'][0]['status'] == 'running':
        r = requests.get(url + '/commands' + data)
        cmd = r.json()
    cmd['data']['commands'][0]['timestamp'] = None
    cmd['data']['commands'][0]['start_time'] = None
    cmd['data']['commands'][0]['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_commands_get_markdown(regtest, db, url, file):
    data = [{
        "sha256_digests": [file['sha256_digest']],
        "scale": "hashes",
        "command": "all",
        "format": "markdown"
    }]
    r = requests.get(url + '/commands', json=data)
    cmd = r.json()
    while cmd['data']['commands'][0]['status'] == 'pending' or \
            cmd['data']['commands'][0]['status'] == 'running':
        r = requests.get(url + '/commands' + data)
        cmd = r.json()
    cmd['data']['commands'][0]['timestamp'] = None
    cmd['data']['commands'][0]['start_time'] = None
    cmd['data']['commands'][0]['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_commands_get_plaintext(regtest, db, url, file):
    data = [{
        "sha256_digests": [file['sha256_digest']],
        "scale": "strings",
        "command": "all_strings",
        "format": "plaintext"
    }]
    r = requests.get(url + '/commands', json=data)
    cmd = r.json()
    while cmd['data']['commands'][0]['status'] == 'pending' or \
            cmd['data']['commands'][0]['status'] == 'running':
        r = requests.get(url + '/commands' + data)
        cmd = r.json()
    cmd['data']['commands'][0]['timestamp'] = None
    cmd['data']['commands'][0]['start_time'] = None
    cmd['data']['commands'][0]['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))


def test_commands_get_incorrect_format(regtest, db, url, file):
    data = [{
        "sha256_digests": [file['sha256_digest']],
        "scale": "hashes",
        "command": "all",
        "format": "abcd"
    }]
    r = requests.get(url + '/commands', json=data)
    regtest.write(r.text)


def test_commands_get_incorrect(regtest, db, url, file):
    data = "?sha256_digest=" + file['sha256_digest'] + \
           "&scale=hashes" + \
           "&command=alls"
    r = requests.get(url + '/commands' + data)
    regtest.write(r.text)


def test_commands_get_incorrect_1(regtest, db, url, file):
    data = "?sha256_digest=" + file['sha256_digest'] + \
           "&scale=hashess"
    r = requests.get(url + '/commands' + data)
    regtest.write(r.text)


def test_commands_get_incorrect_2(regtest, db, url):
    data = "?sha256_digest=abcd"
    r = requests.get(url + '/commands' + data)
    regtest.write(r.text)


def test_commands_get_args_present(regtest, db, url ,interesting):
    data = "?sha256_digest=" + interesting['sha256_digest'] + \
           "&scale=strings" + \
           "&command=interesting" + \
           "&args[min_length]=10"
    r = requests.get(url + '/commands' + data)
    cmd = r.json()
    cmd['data']['commands'][0]['timestamp'] = None
    cmd['data']['commands'][0]['start_time'] = None
    cmd['data']['commands'][0]['end_time'] = None
    regtest.write(str(json.dumps(cmd, sort_keys=True)))