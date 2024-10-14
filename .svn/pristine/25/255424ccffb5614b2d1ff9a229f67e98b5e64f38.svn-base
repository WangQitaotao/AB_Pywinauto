# -*- encoding: utf-8 -*-
'''
@时间 ： 2024/7/16 14:49
@作者 ： WangQitao
@名称 ： main.py
@描述 ：
'''
import multiprocessing
import shutil
import sys
import os

from common.read_yaml import ReadYaml
from testcaseAB.test_pro import run_prodemo
from tools.run_cmd import pa_install
from tools.startAB import get_version
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
import time
from tools.operationgoogle import open_google, close_chrome_process

"""
注意事项：
1、软件运行的时候，会自动杀死谷歌浏览器、Excel的进程、获取软件所在的位置并写入数据到yaml文件中
2、构造环境，存在三块磁盘（磁盘0-系统盘，磁盘1-上面有多个分区）
3、软件运行，初始界面是以默认磁盘0(系统盘)，分区是以L分区为基准。 可以更改common下PAXY.py文件 partition_L 参数
4、需要修改软件的安装位置，在tools下startPA.py文件
5、需要将谷歌浏览器设置为默认浏览器，并去电脑设置 网络和Internet中 设置手动代理
"""


if __name__ == '__main__':
    try:
        multiprocessing.freeze_support()    # 这里必须要，不然执行exe程序时会重复执行input相关代码
        print("------------------> 开始执行AB脚本 <------------------")
        print("------------------> 正在检测运行环境 <------------------")
        get_version = get_version()
        time.sleep(1)
        version = int(input('''
        测试的版本
        1 Standard
        2 ProDemo
        3 SrvDemo
        4 TechDemo
        5 UnlDemo
        直接输入对应的序列号：
        '''))
        if get_version == version:
            print("执行测试的版本与本机版本匹配")
        else:
            print("执行测试的版本与本机版本不匹配")
            install = input("是否需要重新安装对应的版本，填 'yes' 或 'no' ：")
            if install == 'yes':
                if version == 1:
                    pa_install("PAssist_Std")
                elif version == 2:
                    pa_install("PAssist_ProDemo")
                elif version == 3:
                    pa_install("PAssist_SrvDemo")
                elif version == 4:
                    pa_install("PAssist_TechDemo")
                elif version == 5:
                    pa_install("PAssist_UnlDemo")
            else:
                print("结束程序")
                sys.exit(0)
        print("------------------> 开始执行脚本 <------------------")
        # 创建一个进程，执行函数，打开浏览器
        open_google_process = multiprocessing.Process(target=open_google)
        open_google_process.start()
        time.sleep(3)
        # 再创建一个进程，执行主函数
        if version == 1:
            ReadYaml().updata_yaml("PAcode", "Excel_sheet", "Standard")
            all_process = multiprocessing.Process(target=run_standard)
        elif version == 2:
            ReadYaml().updata_yaml("PAcode", "Excel_sheet", "ProDemo")
            all_process = multiprocessing.Process(target=run_prodemo)
        elif version == 3:
            ReadYaml().updata_yaml("PAcode", "Excel_sheet", "SrvDemo")
            all_process = multiprocessing.Process(target=run_srvdemo)
        elif version == 4:
            ReadYaml().updata_yaml("PAcode", "Excel_sheet", "TechDemo")
            all_process = multiprocessing.Process(target=run_techdemo)
        elif version == 5:
            ReadYaml().updata_yaml("PAcode", "Excel_sheet", "UnlDemo")
            all_process = multiprocessing.Process(target=run_unldemo)
        # 启动这两个进程
        all_process.start()
        all_process.join()
        time.sleep(3)
        # 判断函数是否执行完成
        if all_process.is_alive() == False:
            # 结束进程，并不是完毕窗口
            all_process.terminate()
            open_google_process.terminate()
        close_chrome_process()
        print("------------------> 程序结束 <------------------")
        print("点击关闭或Enter退出...")
        print(input())
    except TypeError as t:
        print(f"TypeError 异常错误：{t}")
    except Exception as e:
        print(f"Exception 异常错误：{e}")

