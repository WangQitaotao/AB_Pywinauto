# -*- encoding: utf-8 -*-
"""
@时间:   2021/11/7 20:52
@作者:   王齐涛
@文件:   all_paths.py
这里是获取所有文件的目录路径，调用的时候直接调用变量就好了
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

# 封装变量路径
CURRENT = os.path.abspath(__file__)   # 当前文件绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__)).replace("/", r"\\")  # 当前所有目录的上级(当前路径的上上级)

# 相关路径
DATA_PATH = os.path.join(BASE_DIR, "data"+os.sep)
LOGS_PATH = os.path.join(BASE_DIR, "logs")
CASE_PATH = os.path.join(BASE_DIR, "testcaseAB"+os.sep)
IMAGES_PATH = os.path.join(BASE_DIR, "images"+os.sep)





