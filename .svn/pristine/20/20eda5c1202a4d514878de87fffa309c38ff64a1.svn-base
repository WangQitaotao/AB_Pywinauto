# -*- encoding: utf-8 -*-
'''
@时间 ： 2022/12/8 9:17
@作者 ： WangQitao
@文件名称： run_cmd.py
'''
import sys
import os
import subprocess
import time
from common.logger_handler import GetLogger
from common.read_yaml import ReadYaml
from tools.operationgoogle import close_chrome_process
from tools.operationwindows import match_windows


sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))


def software_install(version):
    """执行cmd命令静默安装，安装包默认存放位置在桌面上"""
    try:
        # 判断是否开启软件，如果开启就自动杀死
        if match_windows((ReadYaml().read_yaml("AB"))["Software_Name"]):
            GetLogger().debug("检测到软件开启，杀死进程")
            os.system('taskkill /F /IM Backupper.exe')
            time.sleep(2)
        software_path = os.path.expanduser(f"~/Desktop/{version}.exe")
        # 如果安装包不存在，提供完整路径地址
        if not os.path.exists(software_path):
            GetLogger().error(f"桌面上不存在名为 {software_path} 的文件。")
            software_path = (input("请输入安装包的完整路径："))
        GetLogger().debug("静默安装软件，请等待...")
        run_cmd(rf'"{software_path}" /silent /LANG=en')
        time.sleep(5)
        # 安装软件成功后，会触发浏览器安装成功网页，所以这里需要关闭
        close_chrome_process()
    except Exception as e:
        GetLogger().error(e)


def run_cmd(cmd_command):
    """
    运行 cmd 命令，并返回输出结果
    :param cmd_command: 要执行的 cmd 命令
    :return: 返回命令执行的输出结果
    """
    try:
        output = subprocess.check_output(cmd_command, shell=True, encoding='utf-8')
        return output
    except subprocess.CalledProcessError as e:
        error_message = f"命令执行失败，返回码: {e.returncode}, 错误信息: {e.output}"
        return error_message
    except Exception as ex:
        return f"发生异常: {ex}"


if __name__ == '__main__':
    software_install("ABServerTrial")
    # result = run_cmd(r'"C:\Users\AOMEI 2021\Desktop\PAssist_ProDemo.exe" /silent /LANG=en')
    # sys.stdout.buffer.write(result.encode('utf-8'))
    