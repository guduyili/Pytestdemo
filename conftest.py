import pytest

@pytest.fixture(scope='function', autouse=True)
def fixture_test(request):
    """前后置处理"""
    print('--------接口测试开始--------')
    yield
    print('--------接口测试结束--------')
