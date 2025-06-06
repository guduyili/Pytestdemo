import logging
import os
import sys

DIR_BASE = os.path.dirname(os.path.dirname(__file__))
sys.path.append(DIR_BASE)

# print(DIR_BASE)

# log日志输出级别
LOG_LEVEL = logging.DEBUG  # 文件
STREAM_LOG_LEVEL = logging.DEBUG  # 控制台

# 接口超时时间，单位/s
API_TIMEOUT = 60

# 文件路径
FILE_PATH = {
    'EXTRACT': os.path.join(DIR_BASE, 'extract.yaml'),
    'CONF': os.path.join(DIR_BASE, 'conf/config.ini')
}
# print(FILE_PATH['CONF'])
