import requests


class SendRequest:

    def __init__(self, cookie=None):
        pass

    def get(self, url, data, header):
        """
        :param url:
        :param data:
        :param header:
        :return:
        """
        if header is None:
            res = requests.get(url=url, params=data)
        else:
            res = requests.get(url=url, params=data, headers=header)

        return res.json()

    def post(self, url, data, header):
        """
        :param url:
        :param data:
        :param header:
        :return:
        """

        if header is None:
            res = requests.post(url=url, data=data)
        else:
            res = requests.post(url=url, data=data, headers=header)
        return res.json()

    def run_main(self, url, data, header, method):
        """
        :param self:
        :param url:
        :param data:
        :param header:
        :param method:
        :return:
        """
        res = None
        ## 统一大写
        if method.upper() == "GET":
            res = self.get(url, data, header)

        elif method.upper() == "POST":
            res = self.post(url, data, header)
        else:
            print('不支持其他请求')
        return res
