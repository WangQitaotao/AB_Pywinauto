# -*- encoding: utf-8 -*-
'''
@时间 ： 2022/10/19 15:28
@作者 ： WangQitao
@文件名称： screen_images.py
'''
import inspect
import sys
import os
import time
from common.read_yaml import ReadYaml
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from common.logger_handler import GetLogger
from common.all_paths import IMAGES_PATH
import aircv
from PIL import ImageGrab
log = GetLogger()


def compare_img(source, target):
    """
    aircv.find_template返回的查找结果：比如{'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    confidence 相似度大于0.85时可以认为查找正确，根据需要做调整。result 目标中心点的坐标，rectangle 目标匹配的四个顶点的坐标
    """
    try:
        img_source = aircv.imread(source)
        img_target = aircv.imread(target)
        match_result = aircv.find_template(img_source, img_target)
        log.debug(f"对比结果：{match_result}")

        if match_result is not None and match_result.get('confidence') > 0.85:
            result = list(match_result['result'])  # 将元组转换为列表以进行修改
            if result is not None:
                result.append(img_source.shape[1])  # 添加其他项目的示例修改
                result.append(img_source.shape[0])  # 添加其他项目的示例修改
                match_result['result'] = tuple(result)  # 将列表转换回元组
            return tuple(map(int, match_result['result']))  # 返回中心坐标
        else:
            log.error("相似度未达到阈值要求或未找到匹配结果")
            return None
    except Exception as e:
        log.error(f"函数 {inspect.stack()[0][3]} : 报错异常 - {e}")  # 获取当前函数名和异常信息


def screen_main_screen():
    """截图软件主界面"""
    time.sleep(1)
    size = ReadYaml().read_yaml("AB")
    img_ready = ImageGrab.grab(eval(size["Size"]))
    img_ready.save(IMAGES_PATH + '/main_screen.png')
    log.debug("截图软件主界面 - 成功")


def screen_main_hide():
    """截图软件主界面和展开选项"""
    time.sleep(1)
    size = ReadYaml().read_yaml("AB")
    img_ready = ImageGrab.grab((eval(size["Size"])[0], eval(size["Size"])[1], eval(size["Size"])[2]+194, eval(size["Size"])[3]))
    img_ready.save(IMAGES_PATH + '/main_hide.png')
    log.debug("截图主界面和展开选项 - 成功")


def judge_img_appear(source, target='main_screen.png'):
    """判断指定的图片是否出现"""
    num = 0
    while True:
        screen_main_screen()    # 最新截图（截图默认尺寸，并不是全屏）
        if compare_img(IMAGES_PATH + source, IMAGES_PATH + target) is not None:
            break
        num += 1
        if num == 12:
            log.error("超过最大次数")
            break
        log.debug(f"循环检测图片是否出现，第 {num} 次")
        time.sleep(5)


if __name__ == '__main__':
    # screen_main_screen()
    # a = (compare_img(IMAGES_PATH + 'main_screen.png', IMAGES_PATH + 'drop_down.png'))
    # print(a[0],a[1])
    screen_main_screen()




# (1)窗体左边离屏幕最左边的距离；
# (2)窗体顶边离屏幕最顶边的距离；
# (3)窗体右边离屏幕最左边的距离；
# (4)窗体底边离屏幕最顶边的距离；