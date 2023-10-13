import requests


def test_get():
    r = requests.get('https://httpbin.ceshiren.com/get', verify=False)
    print(r.text)


url = 'https://httpbin.ceshiren.com/'


def test_send_hobby():
    payload = {
        'name': 'lily',
        'hobby': 'sing'
    }
    new_url = url + 'name=hy&hobby=dance'
    resp = requests.get(new_url, payload, verify=False)
    print(resp.json)


def test_send_header():
    my_headers = {
        'name': 'hy',
        'hobby': 'sing'
    }
    new_url = url + 'name=hy&hobby=dance'
    resp = requests.get(url, headers=my_headers, verify=False)
    print(resp.json)


def test_post_url():
    post_url = 'https://httpbin.ceshiren.com/post'
    proxies = {
        "http": "127.0.0.1:8888",
        "https": "127.0.0.1:8888",
    }
    resp = requests.delete(post_url, proxies=proxies, verify=False)
    print(resp.text)
