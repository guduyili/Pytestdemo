import os

import pytest

if __name__ == '__main__':
    # pytest.main(['-vs', './testcase', '-n 3'])
    pytest.main()
    os.system(f'allure serve ./report/temp')