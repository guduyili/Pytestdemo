import random
import requests
from readyaml import ReadYamlData


class DebugTalk:

    def __init__(self):
        self.read = ReadYamlData()

    def get_extract_data(self, node_name, randoms=None):
        """
        获取extract.yaml数据，首先判断randoms是否为数字类型，如果不是就获取下一个node节点的数据
        :param node_name:
        :param randoms:
        :return:
        """
        data = self.read.get_extract_yaml(node_name)

        if randoms is not None:
            randoms = int(randoms)
            data_value = {
                randoms: self.get_extract_order_data(data, randoms),
                0: random.choice(data),
                -1: ','.join(data),
                -2: ','.join(data).split(',')
            }
            data = data_value[randoms]
        else:
            data = self.read.get_extract_yaml(node_name)
        return data

    def get_extract_order_data(self, data, randoms):
        """获取extract.yaml数据，不为0、-1、-2，则按顺序读取文件key的数据"""
        if randoms not in [0,-1,-2]:
            return data[randoms - 1]

if __name__ == '__main__':
    debug = DebugTalk()
    res = debug.get_extract_data('goodIds',3)
    print(res)