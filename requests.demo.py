import requests


from requests import utils

url = 'http://127.0.0.1:8787/dar/user/login'

headers = {}

data = {
    "user_name": "test01",
    "passwd": "admin123"
}

# post
# ret = requests.post(url=url, data=data)
# print(ret.text)

session = requests.session()

ret = session.request(method='post', url=url, data=data)
cookie = requests.utils.dict_from_cookiejar(ret.cookies)

print(cookie)


