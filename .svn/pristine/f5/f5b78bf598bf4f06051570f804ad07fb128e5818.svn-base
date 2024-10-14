# -*- encoding: utf-8 -*-
'''
@时间 ： 2022/10/14 14:49
@作者 ： WangQitao
@文件名称： startAB.py
'''
import sys
import os
import time
from common.read_yaml import ReadYaml
from tools.screen_images import screen_main_screen, judge_img_appear

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from pywinauto import Application
from common.logger_handler import GetLogger
from tools.operationwindows import match_windows_return_text, popup_windows, get_software_size, match_windows_accurate, \
    match_windows

log = GetLogger()


def start_ab(path=r"C:\Program Files (x86)\AOMEI\AOMEI Backupper\ABLauncher.exe"):
    """启动软件"""
    software_name = (ReadYaml().read_yaml("AB"))["Software_Name"]
    if match_windows_accurate(software_name) is not False:
        log.debug("检测到软件正在运行中")
    else:
        log.debug("没有检测到软件运行，触发软件运行")
        Application(backend="uia").start(rf"{path}")  # 启动
        judge_img_appear(source='main_interface.png')
        time.sleep(2)
    popup_windows(match_windows_return_text(software_name))    # 软件置顶显示
    get_software_size()     # 获取软件大小
    time.sleep(2)


if __name__ == '__main__':
    start_ab()


# def kill_ab():
#     """杀死进程关闭软件"""
#     os.system('taskkill /F /IM PartAssist.exe')
#     log.debug("关闭软件")
#     time.sleep(1)
#
#
# def get_version():
#     """
#     查看[Product Version]参数：
#     2 ProDemo
#     3 SrvDemo
#     4 TechDemo
#     5 UnlDemo
#     """
#     config = configparser.ConfigParser()
#     config.read(r"C:\Program Files (x86)\AOMEI Partition Assistant\cfg.ini")
#     if config.has_section('Product Version'):
#         value = config.get('Product Version', 'v')
#         if value == "2":
#             log.debug("当前系统安装版本为： ProDemo 版")
#             return 2
#         elif value == "3":
#             log.debug("当前系统安装版本为： SrvDemo 版")
#             return 3
#         elif value == "4":
#             log.debug("当前系统安装版本为： TechDemo 版")
#             return 4
#         elif value == "5":
#             log.debug("当前系统安装版本为： UnlDemo 版")
#             return 5
#         else:
#             log.debug("其他版本")
#             return 6
#     else:
#         log.debug("当前系统安装版本为： Std 版")
#         return 1
#
#
# def first_run():
#     """判断是否首次运行"""
#     config = configparser.ConfigParser()
#     config.read(r"C:\Program Files (x86)\AOMEI Partition Assistant\Other.ini")
#     # 判断键是否存在
#     if config.has_section('Run'):
#         log.debug("配置文件Other.ini中 键 [Run] 存在,软件不是首次运行")
#     else:
#         log.error("配置文件Other.ini中 键 [Run] 不存在，软件是首次运行，修改配置文件增加键值对")
#         if not config.has_section('Run'):
#             config.add_section('Run')
#         config.set('Run', 'run', '1')
#         # 保存修改后的INI文件
#         with open(r"C:\Program Files (x86)\AOMEI Partition Assistant\Other.ini", 'w') as configfile:
#             config.write(configfile)
#             log.debug("写入成功")
#
#
# def left_pop_up():
#     """判断左下角营销弹窗"""
#     utc_timestamp = calendar.timegm(datetime.utcnow().timetuple())
#     folder_path = "C:\Program Files (x86)\AOMEI Partition Assistant"  # 指定文件夹的路径
#     ini_file_name = "poped.ini"  # 要检查的ini文件名
#     ini_file_path = os.path.join(folder_path, ini_file_name)  # 拼接ini文件的完整路径
#     # 检查文件是否存在
#     if not os.path.exists(ini_file_path):
#         log.debug(f"该文件夹 {ini_file_name} 不存在")
#         # 创建一个新的ini文件
#         config = configparser.ConfigParser()
#         config['main'] = {'count': '1'}
#         config['Poped1'] = {'ID': '252', 'time': f'{utc_timestamp}', 'uninterest': '0'}
#         # 写入数据到ini文件
#         with open(ini_file_path, 'w') as configfile:
#             config.write(configfile)
#             log.debug("写入文件成功")
#     else:
#         log.error(f"该文件夹 {ini_file_name} 存在")


