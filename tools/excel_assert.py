# -*- encoding: utf-8 -*-
'''
@时间 ： 2022/2/26 21:05
@作者 ： 王齐涛
@文件名称： excel_assert.py 
'''
import inspect
import sys
import os

from common.read_yaml import ReadYaml

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
import time
from tools.excel_openyxl_data import HandleExcel
from common.logger_handler import GetLogger


class ExcelAssert:
    sheet_name = (ReadYaml().read_yaml("AB"))["Excel_sheet"]
    excel_task = HandleExcel(sheet_name=f"{sheet_name}")  # Excel实例化对象并获取数据
    args = excel_task.get_test_case()

    def __init__(self):
        self.log = GetLogger()

    def assert_message(self, expect_message, actual_message, row):
        """
        断言操作，判断结果是否相等，检测Excel表格中的数据
        :param expect_message: 预期结果，从Excel中获取拼接的url
        :param actual_message: 实际结果，通过打开网页获取到的url
        :param row: 当前用例所在的行数
        :return:
        """
        try:
            if expect_message == actual_message:
                self.log.debug(f"断言检查点：预期Excel结果  \n{expect_message}")
                self.log.debug(f"断言检查点：实际Webpg结果  \n{actual_message}")
                self.log.info("断言成功")
                self.excel_task.write_test_data(row=row, column=16, value=actual_message)
                self.excel_task.write_test_data(row=row, column=17, value="pass")
                self.log.debug("执行结果- pass 写入Excel")
            else:
                self.log.debug(f"断言检查点：预期Excel结果  \n{expect_message}")
                self.log.debug(f"断言检查点：实际Webpg结果  \n{actual_message}")
                self.log.error(f"----> 断言失败 <----")
                self.excel_task.write_test_data(row=row, column=16, value=actual_message)
                self.excel_task.write_test_data(row=row, column=17, value="fail")
                self.log.debug("执行结果- fail 写入Excel")
        except RuntimeError as r:
            self.log.error(f"函数 {inspect.stack()[0][3]} :拒绝访问，可能是Excel已经被打开，请关闭Excel后再试。{r}")
        except Exception as e:
            self.log.error(f"函数 {inspect.stack()[0][3]} : 报错异常 - {e}")


def template_print(idx):
    ExcelAssert().log.info(f" --------- 当前运行的功能模块 ： {(ExcelAssert.args)[idx]['entrance']}")


if __name__ == '__main__':
    pass