import time

import pytest

class TestLogin:

    @pytest.mark.run(order=3)
    def test_case01(self):
        time.sleep(2)
        print("测试一")

    @pytest.mark.run(order=2)
    def test_case02(self):
        time.sleep(2)
        print("测试二")

    @pytest.mark.run(order=1)
    def test_case03(self):
        time.sleep(2)
        print("测试三")