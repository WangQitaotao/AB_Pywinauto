# -*- encoding: utf-8 -*-
'''
@时间 ： 2024/7/16 11:44
@作者 ： WangQitao
@名称 ： test_pro.py
@描述 ：
'''
import sys
import os

from common.read_yaml import ReadYaml

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from testcaseAB.test_method import *
from tools.excel_openyxl_data import HandleExcel
from tools.operationgoogle import operation_debug_google
from tools.startAB import start_ab


def run_prodemo():
    try:
        driver = operation_debug_google()   # 与浏览器建立调试
        start_ab()  # 启动软件
        software_name = (ReadYaml().read_yaml("PAcode"))["Excel_sheet"]
        args = HandleExcel(sheet_name=f"{software_name}").get_test_case()   # Excel实例化对象并获取数据
        for idx in range(0, len(args)):
            # 软件首页
            if args[idx]['entrance'] == '首页-升级' and args[idx]['start'] == 1:
                template_shouyebuynow(driver, idx)
    except Exception as e:
        print(e)
