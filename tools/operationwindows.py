# -*- encoding: utf-8 -*-
'''
@时间 ： 2022/10/9 9:45
@作者 ： WangQitao
@文件名称： operationwindows.py 
'''
import sys
import os

from common.read_yaml import ReadYaml

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
import time
import win32com.client
import win32con
import win32gui
from common.logger_handler import GetLogger

log = GetLogger()


def popup_windows(windows_name):
    """
    弹出窗口，并且置顶显示。前提是该应用必须在Windows窗口中已经打开
    :param name:
    :return:
    """
    try:
        hwnd = win32gui.FindWindow(None, windows_name)
        win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
        shell = win32com.client.Dispatch("WScript.Shell")
        # #先发送一个alt key事件
        shell.SendKeys('%')
        # 设置为当前活动窗口
        win32gui.SendMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
        win32gui.SetForegroundWindow(hwnd)
        # win32gui.ShowWindow(hwnd, win32con.SW_SHOWMAXIMIZED)    # 最大化操作
        time.sleep(2)
        log.debug(f"软件：{windows_name} ，弹出窗口并且置顶显示。")
    except Exception as e:
        log.error(f"窗口：{windows_name} 不存在。代码报错{e}")


def match_windows(win_title):
    """
    查找指定窗口,模糊匹配
    :param win_title: 窗口名称
    :return: 句柄列表
    """
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            win_text = win32gui.GetWindowText(hwnd)
            # 模糊匹配
            if win_text.find(win_title) > -1:
                hwnds.append(hwnd)
        return True
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)  # 列出所有顶级窗口，并传递它们的指针给callback函数
    return hwnds


def win_active(win_title):
    """
    激活指定窗口
    :param win_title: 窗口名称
    :return:
    """
    assert win_title, "win_title不能为空！"
    hwnds = match_windows(win_title)
    if hwnds:
        win32gui.ShowWindow(hwnds[0], win32con.SW_SHOWNORMAL)  # SW_SHOWNORMAL 默认大小，SW_SHOWMAXIMIZED 最大化显示
        win32gui.SetForegroundWindow(hwnds[0])
        win32gui.SetActiveWindow(hwnds[0])


def get_hwnd_dic(hwnd, hwnd_title):
    if (win32gui.IsWindow(hwnd)
            and win32gui.IsWindowEnabled(hwnd)
            and win32gui.IsWindowVisible(hwnd)
            and win32gui.GetWindowText(hwnd)):
        hwnd_title[f"{hwnd}"] = win32gui.GetWindowText(hwnd)


def get_hwnd():
    """
    获取桌面上的所有窗口句柄
    :return: {hwnd:title}
    """
    hwnd_title = {}
    win32gui.EnumWindows(get_hwnd_dic, hwnd_title)
    return hwnd_title


def match_windows_return_text(win_title):
    """
    模糊匹配窗口标题，返回完整名称
    :param win_title: 窗口名称
    :return: 包含窗口标题文本的列表
    """
    try:
        def callback(hwnd, window_titles):
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                win_text = win32gui.GetWindowText(hwnd)
                if win_text.find(win_title) > -1:
                    window_titles.append(win_text)
            return True
        window_titles = []
        win32gui.EnumWindows(callback, window_titles)
        if window_titles:
            return window_titles[0]
        else:
            raise Exception("未找到匹配的窗口标题口")
    except Exception as e:
        log.error(e)


def match_windows_accurate(win_title):
    """
    查找指定窗口,精准匹配
    :param win_title: 窗口名称
    :return: 句柄列表
    """
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            win_text = win32gui.GetWindowText(hwnd)
            # 精确匹配，比较窗口标题是否完全一致
            if win_text == win_title:
                hwnds.append(hwnd)
        return True
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)  # 列出所有顶级窗口，并传递它们的指针给callback函数
    return True if hwnds else False


def check_window_existence(title):
    """等待直到找到指定标题的窗口，传入["test1", "test2"]"""
    if isinstance(title, str):
        titles = [title]
    elif isinstance(title, list):
        titles = title
    else:
        raise ValueError("标题必须是字符串或字符串列表")
    n = 0
    while True:
        found = False
        for title in titles:
            hwnd = win32gui.FindWindow(None, title)
            if hwnd != 0:
                log.debug(f"窗口 '{title}' 已找到，句柄为: {hwnd}")
                found = True
                break
        if found:
            break
        if n == 5:
            log.debug("超过最大次数")
            break
        else:
            log.debug("未找到，继续查找...")
            n += 1
            time.sleep(2)  # 每秒查找一次


def get_software_size():
    """获取软件的尺寸大小"""
    fuzzy_matching_name = match_windows_return_text("傲梅轻松备份")
    complete_name = win32gui.FindWindow(None, f"{fuzzy_matching_name}")
    handle_size = win32gui.GetWindowRect(complete_name)
    ReadYaml().updata_yaml("AB", "Size", f"{handle_size}")
    log.debug(f"成功获取软件的坐标，写入到yaml文件中")


if __name__ == '__main__':
    # print(match_windows_accurate("AOMEI Partition Assistant"))
    # get_software_size()
    # time.sleep(1)
    print(get_hwnd())

