# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/9/30 15:26
@作者 ： 王齐涛
@文件名称： read_yaml.py
'''
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
import yaml
from common.all_paths import DATA_PATH
from common.logger_handler import GetLogger
class ReadYaml:

    def __init__(self):
        self.log = GetLogger()

    def read_yaml(self, filename):
        """
        读yaml文件
        :param filename:
        :return:
        """
        try:
            with open(DATA_PATH + filename + ".yaml", encoding="utf-8", mode="r") as f:
                all_data = yaml.load(stream=f, Loader=yaml.FullLoader)   # 表示加载的方式
            return all_data
        except FileNotFoundError as f:
            self.log.error(f"代码本身报错：{f}")
            self.log.error("你输入的文件名不正确或者文件不存在。")
        except UnicodeDecodeError as u:
            self.log.error(f"代码本身报错：{u}")
            self.log.error("你编辑的yaml文件内容格式可能不正确。")

    def write_yaml(self, filename, data):
        """
        写yaml文件
        :param filename:
        :param data:
        :return:
        """
        try:
            with open(DATA_PATH + filename + ".yaml",  encoding="utf-8", mode="w") as f:
                yaml.dump(data, stream=f, allow_unicode=True)
            self.log.info(f"数据成功写入到文件：{filename}，内容如下：{data}")
        except Exception as e:
            self.log.error(f"代码报错{e}")

    def clear_yaml(self, filename):
        """
        清空yaml数据
        :param filename:
        :return:
        """
        try:
            with open(filename + ".yaml", encoding="utf-8", mode="w") as f:
                f.truncate()
            # self.log.info("数据全部清空啦！！！")
        except Exception as e:
            self.log.error(f"代码报错{e}")

    def updata_yaml(self, filename, k, v):
        """更新yaml数据"""
        old_data = ReadYaml().read_yaml(filename)       # 读取文件数据
        old_data[k] = v                   # 修改读取的数据（k存在就修改对应值，k不存在就新增一组键值对）
        with open(DATA_PATH+filename + ".yaml", "w", encoding="utf-8") as f:
            yaml.dump(old_data, f)


if __name__ == '__main__':
    pass