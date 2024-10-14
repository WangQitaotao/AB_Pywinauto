# -*- encoding: utf-8 -*-
'''
@时间 ： 2024/8/2 15:18
@作者 ： WangQitao
@名称 ： demo1.py 
@描述 ：
'''
import sys
import os

import yaml
from future.backports import urllib

from common.read_yaml import ReadYaml
from screeninfo import get_monitors

# 获取计算机的屏幕信息
monitors = get_monitors()

# 获取屏幕数量
num_screens = len(monitors)
print(f"计算机有 {num_screens} 个屏幕")

# 打印每个屏幕的分辨率
for i, monitor in enumerate(monitors, start=1):
    print(f"屏幕 {i} 分辨率: {monitor.width}x{monitor.height}")


