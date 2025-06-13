import logging
import os
import time
from logging.handlers import RotatingFileHandler

from conf import setting

# 1. 日志文件路径配置
log_path = setting.FILE_PATH['LOG']
print(log_path)
if not os.path.exists(log_path):
    os.mkdir(log_path)

# 2. 日志文件名生成（按日期命名）
logfile_name = log_path + r'\test.{}.log'.format(time.strftime("%Y%m%d"))


class RecordLog:
    """封装日志记录功能的类，提供统一的日志输出接口"""

    def output_logging(self):
        """获取并配置logger对象，返回可用于记录日志的logger实例"""
        # 获取名为__name__的logger实例
        logger = logging.getLogger(__name__)

        # 3. 防止日志重复记录的关键逻辑
        if not logger.handlers:
            # 设置日志级别（从配置文件中获取）
            logger.setLevel(setting.LOG_LEVEL)

            # 4. 定义日志格式
            log_format = logging.Formatter(
                '%(levelname)s - %(asctime)s - %(filename)s:%(lineno)d -[%(module)s:%(funcName)s] - %(message)s')

            # 5. 配置滚动日志处理器
            fh = RotatingFileHandler(
                filename=logfile_name,  # 日志文件路径
                mode='a',  # 追加模式
                maxBytes=5242880,  # 单个日志文件最大5MB(5*1024*1024)
                backupCount=7,  # 最多保留7个历史日志文件
                encoding='utf-8'  # 日志文件编码
            )

            # 设置处理器的日志级别和格式
            fh.setLevel(setting.LOG_LEVEL)
            fh.setFormatter(log_format)

            # 将处理器添加到logger中
            logger.addHandler(fh)

        # 返回配置好的logger实例
        return logger


# 创建日志记录器实例
apilog = RecordLog()
# 获取可用于记录日志的logger对象
logs = apilog.output_logging()