import json
from typing import Any, Dict, List, Optional, Union
from common.debugtalk import DebugTalk
from common.readyaml import get_test_yaml
from common.readyaml import ReadYamlData


class SafeFuncExecutor:
    """安全的函数执行器，限制可调用的函数范围"""

    def __init__(self, allowed_funcs: Optional[Dict[str, callable]] = None):
        self.allowed_funcs = allowed_funcs or {}

    def register(self, name: str, func: callable()):
        """注册允许调用的函数"""
        self.allowed_funcs[name] = func

    def execute(self, name: str, *args) -> Any:
        """执行注册过的函数"""
        if name not in self.allowed_funcs:
            raise ValueError(f"函数 '{name}' 未注册，禁止调用")
        return self.allowed_funcs[name](*args)


def replace_load2(data:Union[Dict, List, str], executor:Optional[SafeFuncExecutor] = None) -> Any:

    # 创建默认执行器并注册允许的函数
    if executor is None:
        executor = SafeFuncExecutor()
        debug_talk = DebugTalk()

        # 注册允许调用的函数（白名单机制）
        # for func_name in ['']:



    return
class BaseRequests:

    def __init__(self):
        self.read = ReadYamlData()

    def replace_load(self, data):
        """"yaml数据替换解析"""
        str_data = data
        if not isinstance(data, str):
            str_data = json.dumps(data, ensure_ascii=False)

        for i in range(str_data.count('${')):
            if "${" in str_data or "}" in str_data:
                start_index = str_data.index('$')
                end_index = str_data.index('}', start_index)
                # print(start_index)
                # print(end_index)
                ref_all_params = str_data[start_index:end_index + 1]
                print(ref_all_params)
                # 取出函数名
                func_name = ref_all_params[2:ref_all_params.index("(")]
                print(func_name)
                # 去除函数中的参数值
                func_params = ref_all_params[ref_all_params.index("(") + 1:ref_all_params.index(")")]
                print(func_params)

                # 传入替换的参数获取对应的值
                # getattr(DebugTalk(), func_name) 动态获取 DebugTalk 类的实例和对应的方法
                # *func_params.split(',') 将参数字符串按逗号分割并解包为多个参数
                extract_data = getattr(DebugTalk(), func_name)(*func_params.split(',') if func_params else "")

                # 如果返回值是列表， 转换为逗号分隔的字符串
                if extract_data and isinstance(extract_data, list):
                    extract_data = ','.join(e for e in extract_data)

                str_data = str_data.replace(ref_all_params, str(extract_data))
                print(str_data)

        # 还原数据 将字典还原为JSON 字符串
        if data and isinstance(data, dict):
            data = json.loads(str_data)
        else:
            data = str_data
        return data




if __name__ == '__main__':
    basequest = BaseRequests()

    data = get_test_yaml('../login.yaml')[0]
    print(data)
    basequest.replace_load(data)
    # print(ret)
