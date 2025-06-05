import json
import os.path
# from debugtalk import DebugTalk
import yaml


def get_test_yaml(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
            return yaml_data
    except Exception as e:
        print(e)


class ReadYamlData:

    # 读入接口提取的变量值
    def get_extract_yaml(self, node_name):
        file_path = 'extract.yaml'
        if os.path.exists(file_path):
            pass
        else:
            file = open(file_path, 'w')
            file.close()

        with open(file_path, 'r', encoding='utf-8') as rf:
            extract_data = yaml.safe_load(rf)
            return extract_data[node_name]

    # 写入extract.yaml数据
    def write_data_yaml(self, value):
        """
        allow_unicode = True表示可以输入中文 sort_keys按顺序写入
        :param self:
        :param value:
        :return:
        """
        file = None
        file_path = 'extract.yaml'
        # 不存在即创建新文件
        if not os.path.exists(file_path):
            os.system(file_path)
        try:
            # a 为append 新增在文件末尾
            file = open(file_path, 'a', encoding='utf-8')
            # 仅处理dict字典类型数据 忽略其他类型
            if isinstance(value, dict):
                # dump 为将py对象转换为yaml
                write_data = yaml.dump(value, allow_unicode=True, sort_keys=False)
                file.write(write_data)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # 获取第一个配置项（假设YAML中包含多个测试用例，仅处理第一个）
    res = get_test_yaml('login.yaml')[0]
    url = res['baseInfo']['url']
    new_url = 'http://127.0.0.1:8787' + url
    method = res['baseInfo']['method']
    data = res['testCase'][0]['data']
    # header = res['']
    from sendrequests import SendRequest

    send = SendRequest()
    res = send.run_main(method=method, url=new_url, data=data, header=None)

    # print(url)
    # print(new_url)
    # print(method)
    # print(data)
    # print(res)

    # 使用write存储token
    write_data = {}
    token = res.get('token')
    write_data['token'] = token
    read = ReadYamlData()
    read.write_data_yaml(write_data)

    # print(token)

    #  JSON 序列化（Python 对象 → JSON 字符串）
    # 概念：将Python对象（如字典、列表）转换为JSON格式的字符串。
    # 函数：json.dumps()（生成字符串）或json.dump()（直接写入文件）。
    json_str = json.dumps(res, ensure_ascii=False)
    # print(json_str)
    # print(type(json_str))

    #  JSON 反序列化（JSON 字符串 → Python 对象）
    # 概念：将JSON格式的字符串解析为Python对象（字典或列表）。
    # 函数：json.loads()（解析字符串）或json.load()（从文件读取）。
    json_dict = json.loads(json_str)
    # print(json_dict)
    # print(type(json_dict))
    #
    # debugtalk = DebugTalk()
    # ret = debugtalk.get_extract_data('goodIds', 0)
    # print(ret)
    res2 = read.get_extract_yaml('goodIds')
    print(res2)