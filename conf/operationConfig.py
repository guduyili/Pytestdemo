import configparser
from conf import setting


class OperationConfig:
    """封装读取*.ini配置文件模块"""

    def __init__(self, file_path=None):

        if file_path is None:
            self.__file_path = setting.FILE_PATH['CONF']
        else:
            self.__file_path = file_path

        self.conf = configparser.ConfigParser()
        try:
            self.conf.read(self.__file_path, encoding='utf-8')
        except Exception as e:
            print(e)

    def get_section_for_data(self, section, option):
        """
        读取ini数据
        :param section:
        :param option:
        :return:
        """
        try:
            data = self.conf.get(section, option)
            return data
        except Exception as e:
            print(e)


    def get_envi(self, option):
        """读取接口服务器ip地址"""
        return self.get_section_for_data('api_envi', option)

if __name__ == '__main__':
    oper = OperationConfig()
    print(oper.get_envi('host'))
    print(oper.get_envi('test'))