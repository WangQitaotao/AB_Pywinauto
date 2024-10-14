# -*- encoding: utf-8 -*-
'''
@时间 ： 2022/9/29 14:39
@作者 ： WangQitao
@文件名称： Base.py 
'''
import inspect
import sys
import os
from common.all_paths import IMAGES_PATH
from common.read_yaml import ReadYaml
from tools.screen_images import compare_img, screen_main_screen
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from pykeyboard import PyKeyboard
from common.logger_handler import GetLogger
import time
import win32api,win32gui,win32con

log = GetLogger()
size = ReadYaml().read_yaml("AB")
software_screen_size = (eval(size["Size"]))


# <<<<<<<<<<<<<<<<<<<             模拟鼠标事件              >>>>>>>>>>>>>>>>>>>
def move_click_coord_relative(xy, click=True):
    """
    相对坐标，基于软件左上角操作  。移动+单击。默认为左击
    :param xy: 传入的是一个元组。比如 （x,y）
    :param click: 是否左击，默认为是
    :return:
    """
    try:
        log.debug(f"鼠标移动到 {(software_screen_size[0] + xy[0], software_screen_size[1] + xy[1])} 处，并进行点击")
        win32api.SetCursorPos((software_screen_size[0] + xy[0], software_screen_size[1] + xy[1]))
        time.sleep(1.5)
        if click:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        else:
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN | win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
    except Exception as e:
        log.error(f"函数 {inspect.stack()[0][3]} : 报错异常 - {e}")


def operation_dropdown_menu():
    """操作软件中的下拉选项"""
    try:
        log.debug("移动界面下拉选项，软件左下角只显示三个磁盘")
        while True:
            screen_main_screen()    # 动态获取界面
            coordinate = compare_img(IMAGES_PATH + 'main_screen.png', IMAGES_PATH + 'drop_down.png')    # 对比后返回照片所在的坐标
            win32api.SetCursorPos((software_screen_size[0] + coordinate[0], software_screen_size[1] + coordinate[1]))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, coordinate[0], coordinate[1], 0, 0)
            time.sleep(2)
            if 390 <= coordinate[1] <= 410:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,  coordinate[0], coordinate[1], 0, 0)
                log.debug("间距在390-410之间，直接跳出循环")
                break  # 如果在390-410之间，直接跳出循环
            # 判断移动方向
            if coordinate[1] < 390:
                direction = 1  # 向下
                scroll_distance = 410 - coordinate[1]
            elif coordinate[1] > 410:
                direction = -1  # 向上
                scroll_distance = coordinate[1] - 390
            else:
                direction = 0  # 不移动
                scroll_distance = 0
            # 根据direction决定滑动方向
            for i in range(scroll_distance):
                if direction == 1:  # 向下移动
                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 1)
                elif direction == -1:  # 向上移动
                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -1)
                else:  # 不移动
                    break
            # 释放鼠标左键
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,  coordinate[0], coordinate[1], 0, 0)
    except Exception as e:
        log.error(f"函数 {inspect.stack()[0][3]} : 报错异常 - {e}")


# <<<<<<<<<<<<<<<<<<<             模拟键盘事件              >>>>>>>>>>>>>>>>>>>>

class KeyBoard:
    """模拟键盘事件"""
    k = PyKeyboard()
    keys = {'A': 65, 'J': 74, 'S': 83, '1': 49, 'B': 66, 'K': 75, 'T': 84, '2': 50, 'C': 67, 'L': 76, 'U': 85, '3': 51,'D': 68, 'M': 77, 'V': 86,
            '4': 52, 'E': 69, 'N': 78, 'W': 87, '5': 53, 'F': 70, 'O': 79, 'X': 88, '6': 54,'G': 71, 'P': 80, 'Y': 89, '7': 55, 'H': 72, 'Q': 81,
            'Z': 90, '8': 56, 'I': 73, 'R': 82, '0': 48, '9': 57, 'F1': 112, 'F7': 118, 'F2': 113, 'F8': 119, '*': 106, 'F3': 114, 'F9': 120,
            'F4': 115, 'F10': 121, 'ENTER': 13, 'F5': 116, 'F11': 122, 'F6': 117, 'F12': 123, '.': 190, 'BACKSPACE': 8, 'CTRL_L': 17,'CTRL': 17,
            'CAPS_LOCK': 4, 'CMD': 91, 'CMD_R': 91, 'MENU': 93, 'ESC': 27, 'RIGHTARROW': 39, '-': 189, 'TAB': 9, 'SPACE': 32, 'DOWNARROW': 40,
            'CLEAR': 12, 'PAGEUP': 33, 'INSERT': 45, '/': 191, 'PAGEDOWN': 34, 'PAGE_DOWN': 34, 'PAGE_UP': 33, 'DELETE': 46, '`': 192, 'SHIFT': 16,
            'END': 35, 'NUMLOCK': 144, '[': 219, 'CONTROL': 17, 'HOME': 36, ';': 186, '\\': 220, 'ALT': 18, 'ALT_L': 18, 'LEFTARROW': 37,'=': 187,
            ']': 221, 'CAPELOCK': 20, 'UPARROW': 38, ',': 188, "'": 222, '"': 'SHIFT+\'', '<': 'SHIFT+,','}': 'SHIFT+]','|': 'SHIFT+\\',
            '+': 'SHIFT+=', '?': 'SHIFT+/', '{': 'SHIFT+[', ':': 'SHIFT+;', '_': 'SHIFT+-', '>': 'SHIFT+.', '~': 'SHIFT+`'
            }

    @staticmethod
    def ctrlV():
        win32api.keybd_event(17, 0, 0, 0)  # ctrl
        win32api.keybd_event(86, 0, 0, 0)  # v
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
        time.sleep(0.5)

    @staticmethod
    def enter():
        win32api.keybd_event(13, 0, 0, 0)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.5)

    @staticmethod
    def ctrlA():
        win32api.keybd_event(17, 0, 0, 0)   # ctrl
        win32api.keybd_event(65, 0, 0, 0)   # a
        win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.5)

    @staticmethod
    def back_del():
        win32api.keybd_event(8, 0, 0, 0)
        win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.5)

    @staticmethod
    def input_data(code):
        KeyBoard.ctrlA()
        time.sleep(0.5)
        KeyBoard.back_del()
        if isinstance(code, int):
            KeyBoard.k.type_string(str(code))
        else:
            KeyBoard.k.type_string(code)
        KeyBoard.enter()
        time.sleep(0.5)


# <<<<<<<<<<<<<<<<<<<             其他操作              >>>>>>>>>>>>>>>>>>>>

def move_mouse_and_scroll(xy):
    """模拟鼠标按下左键，再移动，最后松开"""
    target_pos = (software_screen_size[0] + xy[0], software_screen_size[1] + xy[1])
    win32api.SetCursorPos(target_pos)
    time.sleep(2)
    # 模拟左键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, target_pos[0], target_pos[1], 0, 0)
    time.sleep(2)
    scroll_distance = 100
    for i in range(scroll_distance):
        # 向左移动1像素
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1, 0, 0, 0)
        # 模拟左键松开
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, target_pos[0], target_pos[1], 0, 0)


def click_left():
    """左键点击"""
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    log.debug(f"鼠标点击事件")


def get_coord():
    """获取当前坐标"""
    log.debug(f"获取当前位置坐标:{win32gui.GetCursorPos()}")
    return win32gui.GetCursorPos()


if __name__ == '__main__':
    operation_dropdown_menu()