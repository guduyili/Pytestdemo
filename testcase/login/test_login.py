# -*- coding: utf-8 -*-
import time
from conftest import fixture_test
import pytest
from common.readyaml import get_test_yaml
from common.sendrequests import SendRequest
from common.recordlog import logs


# @pytest.fixture(scope='function', autouse=True)
# def fixture_test(request):
#     """前后置处理"""
#     print('--------接口测试开始--------')
#     yield
#     print('--------接口测试结束--------')

class TestLogin:
    #
    # # @pytest.mark.run(order=3)
    # # @pytest.mark.smoke
    # # @pytest.mark.parametrize('params', ['test','case','exit'])
    # @pytest.mark.parametrize('params', ["姜维", '伯约', '大统领'])
    # def test_case01(self, params, fixture_test):
    #     # time.sleep(2)
    #     print("测试一")
    #     print("获取的参数",params)
    #
    # # @pytest.mark.run(order=2)
    # def test_case02(self, fixture_test):
    #     # time.sleep(2)
    #     print("测试二")
    #
    # # @pytest.mark.run(order=1)
    # # @pytest.fixture()
    # def test_case03(self, fixture_test):
    #     # time.sleep(2)
    #     print("测试三")
    @pytest.mark.parametrize('params', get_test_yaml('./testcase/login/login.yaml'))
    def test_03(self, params):
        # print(params)
        baseInfo = params['baseInfo']
        print(baseInfo)

        url = params['baseInfo']['url']
        new_url = 'http://127.0.0.1:8787' + url
        logs.info("LOG输出url {}" .format(new_url))

        method = params['baseInfo']['method']
        headers = params['baseInfo']['header']

        # params['testCase'][0]：获取第一个测试用例（索引0）。
        # params['testCase'][0]['data']：从第一个测试用例中获取data字段
        data = params['testCase'][0]['data']

        send = SendRequest()
        ret = send.run_main(url=new_url, method=method, header=None, data=data)
        print(ret)
        assert ret['msg'] == '登录成功'

    @pytest.mark.parametrize('params', get_test_yaml('./testcase/login/login.yaml'))
    def test_04(self, params):
        # print(params)
        baseInfo = params['baseInfo']
        print(baseInfo)

        url = params['baseInfo']['url']
        new_url = 'http://127.0.0.1:8787' + url

        method = params['baseInfo']['method']
        headers = params['baseInfo']['header']

        # params['testCase'][0]：获取第一个测试用例（索引0）。
        # params['testCase'][0]['data']：从第一个测试用例中获取data字段
        data = params['testCase'][0]['data']

        send = SendRequest()
        ret = send.run_main(url=new_url, method=method, header=None, data=data)
        print(ret)
        assert ret['msg'] == '登录失败'
