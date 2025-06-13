import sys

import pytest

@pytest.fixture(scope='function', autouse=True)
def fixture_test(request):
    """前后置处理"""
    print('--------接口测试开始--------')
    yield
    print('--------接口测试结束--------')


def pytest_configure(config):
    # 设置标准输出编码为UTF-8
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
