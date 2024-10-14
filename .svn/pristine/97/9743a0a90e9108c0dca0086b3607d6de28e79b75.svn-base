# -*- encoding: utf-8 -*-
'''
@时间 ： 2022/10/9 15:51
@作者 ： WangQitao
@文件名称： operationgoogle.py 
'''
import inspect
import subprocess
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from selenium.common import TimeoutException
import time
from common.logger_handler import GetLogger
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import psutil
log = GetLogger()


def close_chrome_process():
    """关闭 Chrome 进程"""
    try:
        log.error("触发程序，关闭 Chrome 浏览器")
        chrome_process_exists = False
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == 'chrome.exe':    # 判断进程是否存在
                chrome_process_exists = True
                break
        if chrome_process_exists:
            os.system('chcp 65001')  # 设置命令行编码为UTF-8
            os.system('taskkill /F /IM chrome.exe')
        time.sleep(2)
        return True
    except subprocess.CalledProcessError as e:
        log.error(f"关闭 Chrome 进程出错: {e}")
        return False


def open_google():
    """打开谷歌浏览器窗口"""
    try:
        log.debug("默认杀死浏览器所有进程")
        close_chrome_process()
        time.sleep(2)
        # log.debug("使用cmd命令打开新的浏览器")
        os.chdir("C:\Program Files\Google\Chrome\Application")     # 切换到当前目录，然后执行cmd命令
        os.system(r"chrome.exe --remote-debugging-port=9222")  # 打开新的浏览器进行监控
    except Exception as e:
        log.error(f"函数 {inspect.stack()[0][3]} : 报错异常 - {e}")


def operation_debug_google():
    """利用Chrome DevTools协议。允许客户检查和调试Chrome浏览器。
    思路：远程调试的模式下打开浏览器，然后AB软件打开网页后，就会基于这个浏览器，这样子结合selenium就好操作获取url了。
    手动方法：打开CMD，跳转到Chrome的安装目录，执行代码：chrome.exe --remote-debugging-port=9222，还有部分参数没有用
    自动方法：调用方法"""
    try:
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")     # 建立通信
        log.debug("正在加载 webdriver.Chrome 中，并与新浏览器建立通信.......")    # 这里有时候很快有时候很慢，不晓得为啥子
        driver = webdriver.Chrome(options=chrome_options)
        log.debug("加载完成")
        return driver
    except TimeoutException as e:
        log.error(f"连接到浏览器超时，请检查远程调试设置和网络连接：{e}")
    except Exception as e:
        log.error(f"函数 {inspect.stack()[0][3]} : 报错异常 - {e}")


def get_all_handle_name(driver):
    """获取浏览器中的所有句柄"""
    handles = driver.window_handles     # 获取所有句柄
    log.debug(f"获取浏览器的所有句柄： {handles}")
    return handles


def switch_new_handle(driver):
    """
    切换至新窗口，并获取当前句柄的url
    :param driver:
    :return:
    """
    handles = driver.window_handles     # 获取所有句柄
    log.debug(f"所有句柄：{handles}")
    driver.switch_to.window(handles[-1])    # 切换到最新窗口
    # log.debug(f"获取当前网页的标题：{driver.title}")
    log.debug(f"获取当前网页的URL：{driver.current_url}")
    time.sleep(0.5)
    return driver.current_url


def close_new_handle(driver):
    """
    关闭新窗口
    :param driver:
    :return:
    """
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])
    time.sleep(0.5)
    driver.close()
    time.sleep(0.5)
    log.debug("关闭当前打开的网页")


def minimize_handle(driver):
    """
    最小化新窗口
    :param driver:
    :return:
    """
    handles = driver.window_handles
    driver.switch_to.window(handles[0])
    time.sleep(0.5)
    driver.minimize_window()
    time.sleep(0.5)
    log.debug("最小化当前网页")


def switch_old_handle(driver):
    """
    切换至旧窗口
    :param driver:
    :return:
    """
    handles = driver.window_handles
    driver.switch_to.window(handles[0])


if __name__ == '__main__':
    close_chrome_process()
    # driver = operation_debug_google()
    # switch_new_window(driver)

