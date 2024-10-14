# -*- encoding: utf-8 -*-
'''
@时间 ： 2022/10/27 11:34
@作者 ： WangQitao
@文件名称： test_method.py
'''
import inspect
import re
import sys
import os

from common.logger_handler import GetLogger
from common.read_yaml import ReadYaml

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from common.all_paths import IMAGES_PATH
from tools.operationwindows import match_windows_accurate, check_window_existence
from tools.screen_images import screen_main_screen, compare_img, screen_main_hide
from tools.decrypt import decrypt_url
from tools.excel_assert import ExcelAssert, template_print
from tools.excel_openyxl_data import HandleExcel
from tools.operationgoogle import switch_new_handle, get_all_handle_name, close_new_handle, minimize_handle
import time
from common.Base import move_click_coord_relative, move_mouse_and_scroll
from common.PAXY import PAXY


sheet_name = (ReadYaml().read_yaml("PAcode"))["Excel_sheet"]
args = HandleExcel(sheet_name=f"{sheet_name}").get_test_case()   # Excel实例化对象并获取数据


# 封装其他方法
def get_assert_url(driver, idx):
    """获取网页中的链接，并解密处理，并将数据写入到Excel中进行对比"""
    try:
        time.sleep(1)
        web_url = switch_new_handle(driver)     # 切换到新打开的浏览器并获取网址
        if len(get_all_handle_name(driver)) == 1:     # 判断句柄的数量是否为1
            GetLogger.error("浏览器窗口曲柄只有一个，不符合逻辑，退出程序！")
            sys.exit()
        if "eurl=" not in web_url:
            GetLogger.error(f"获取到的是跳转后的链接：{web_url}，不符合底代码逻辑，退出程序！")
            sys.exit()
        time.sleep(0.5)
        close_new_handle(driver)    # 关闭句柄
        minimize_handle(driver)     # 最小化句柄
        # contains_control_chars = any(re.match(r'[\x00-\x1F\x7F]', char) for char in decrypt_url((web_url.split("eurl="))[1])
        # if contains_control_chars:
        new_url = re.sub(r'[\x00-\x1F\x7F]', '', decrypt_url((web_url.split("eurl="))[1]))  # 处理解密后链接空格问题
        expect_url = args[idx]["link"]+"&popul="+args[idx]["popul"]+f"?source={args[idx]['source']}&lang={args[idx]['lang']}&edition={args[idx]['edition']}&ver={args[idx]['ver']}&useday={args[idx]['useday']}&status={args[idx]['status']}&plan={args[idx]['plan']}&sn={args[idx]['sn']}&n_refs={args[idx]['n_refs']}&did={args[idx]['did']}"
        ExcelAssert().assert_message(expect_message=expect_url, actual_message=new_url, row=idx+2)      # 这里idx要加2，才能匹配到Excel对应的行数
    except Exception as e:
        GetLogger.error(f"函数 {inspect.stack()[0][3]} : 报错异常 - {e}")


def marketing_window_year_subscription(driver, idx):
    """营销购买窗口-年度订阅"""
    time.sleep(1)
    move_click_coord_relative(PAXY().marketing_window_year_subscription)
    get_assert_url(driver, idx)


def marketing_window_lifetime_upgrade(driver, idx):
    """营销购买窗口-终身升级"""
    time.sleep(1)
    move_click_coord_relative(PAXY().marketing_window_lifetime_upgrade)
    get_assert_url(driver, idx)


def marketing_window_lifetime_family(driver, idx):
    """营销购买窗口-家庭终身"""
    time.sleep(1)
    move_click_coord_relative(PAXY().marketing_window_lifetime_family)
    get_assert_url(driver, idx)


def marketing_window_all(driver, idx):
    """营销窗口的三个购买结合到一个方法中"""
    marketing_window_year_subscription(driver, idx)
    marketing_window_lifetime_upgrade(driver, idx+1)
    marketing_window_lifetime_family(driver, idx+2)
    move_click_coord_relative(PAXY().marketing_window_close)    # 关闭营销窗口
    time.sleep(2)


def template_top_left_apply():
    """左上角执行等待程序"""
    move_click_coord_relative(PAXY().top_left_apply)
    check_window_existence(["擱置作業", "Pending Operations"])
    move_click_coord_relative(PAXY().top_left_apply_P)


def template_top_refresh():
    """顶部-刷新按钮：一种情况是没有等待执行的程序，直接刷新；另一个是有等待执行的程序，会弹个提示窗口再刷新"""
    move_click_coord_relative(PAXY().top_refresh)
    time.sleep(1)
    if match_windows_accurate("AOMEI Partition Assistant") is True:
        print("检测到有确认窗口，点击是")
        move_click_coord_relative(PAXY().top_refresh_Y)
    else:
        print("没有检测到确认窗口，直接刷新")
    time.sleep(4)


def judge_img_appear(img):
    """判断指定的图片是否出现"""
    num = 0
    while True:
        time.sleep(5)
        screen_main_screen()    # 最新截图（截图默认尺寸，并不是全屏）
        if compare_img(IMAGES_PATH + 'main_screen.png', IMAGES_PATH + img) is not None:
            break
        num += 1
        print(f"循环检测图片是否出现，第 {num} 次")


# 封装的程序点击事件
def template_shouyebuynow(driver, idx):
    """顶部-立即购买"""
    template_print(idx)
    screen_main_screen()
    move_click_coord_relative(compare_img(IMAGES_PATH + 'main_screen.png', IMAGES_PATH + 'upgrade.png'))
    marketing_window_all(driver, idx)


# def template_left_hide_partition_alignment(driver, idx):
#     template_print(idx)
#     move_click_coord_relative(PAXY().partition_L)
#     screen_main_screen()
#     move_click_coord_relative(compare_img(IMAGES_PATH + 'main_screen.png', IMAGES_PATH + 'hide.png'))
#     screen_main_hide()    # 截图展开选项
#     move_click_coord_relative(compare_img(IMAGES_PATH + 'main_hide.png', IMAGES_PATH + 'std_hide_partition_alignment.png'))
#     move_click_coord_relative(PAXY().hide_hide_partition_O)
#     marketing_window_all(driver, idx)
#     move_click_coord_relative(PAXY().allocate_free_space_O_std)
