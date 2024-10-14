# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/11/8 22:21
@作者 ： 王齐涛
@文件名称： times.py
'''
import time
import datetime
from functools import wraps
from common.logger_handler import GetLogger
log = GetLogger()


def timestamp():
    """时间戳"""
    return time.time()


def dt_strftime(fmt="%Y%m"):
    """
    datetime格式化时间
    :param fmt "%Y%m%d %H%M%S
    """
    return datetime.datetime.now().strftime(fmt)


def sleep(seconds=1.0):
    """
    睡眠时间
    """
    time.sleep(seconds)


def running_time(func):
    """统计函数的运行时间"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = timestamp()
        res = func(*args, **kwargs)
        log.info("代码执行完成！用时%.3f秒！" % (timestamp() - start))
        all_time(timestamp() - start)
        return res
    return wrapper


def all_time(time):
    if time <= 60:
        log.info(f"代码执行完成！用时{time}秒！")
    if time > 60 and time < 3600:
        minute = time // 60
        sec = time % 60
        log.info(f"代码执行完成！用时{minute}分钟{sec}秒！")
    if time >= 3600 and time <= 86400:
        days = time // 3600
        minute = time % 3600 / 60
        log.info(f"代码执行完成！用时{days}小时{minute}分钟！")


if __name__ == '__main__':
    # print(dt_strftime("%Y%m%d%H%M%S"))
    all_time(7201)