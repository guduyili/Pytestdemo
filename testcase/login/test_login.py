import time
from conftest import fixture_test
import pytest

# @pytest.fixture(scope='function', autouse=True)
# def fixture_test(request):
#     """前后置处理"""
#     print('--------接口测试开始--------')
#     yield
#     print('--------接口测试结束--------')

class TestLogin:

    @pytest.mark.run(order=3)
    # @pytest.mark.smoke
    def test_case01(selft):
        # time.sleep(2)
        print("测试一")

    @pytest.mark.run(order=2)
    def test_case02(self):
        # time.sleep(2)
        print("测试二")

    @pytest.mark.run(order=1)
    # @pytest.fixture()
    def test_case03(self):
        # time.sleep(2)
        print("测试三")