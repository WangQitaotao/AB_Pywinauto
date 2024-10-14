# -*- encoding: utf-8 -*-
"""
@时间:   2021/11/7 11:10
@作者:   王齐涛
@文件:   conftest.py
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
import time
import pytest
from common.all_paths import DATA_PATH, BASE_DIR
from common.logger_handler import GetLogger

log = GetLogger()

@pytest.fixture()
def setup_teardown():
    log.info(" -----> 测试开始 <----- ")
    yield
    log.info(" -----> 测试结束 <----- ")


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    '''
    收集用例的执行结果
    :param terminalreporter:
    :param exitstatus:
    :param config:
    :return:
    '''
    # print(terminalreporter.stats)
    total = terminalreporter._numcollected
    passed = len(terminalreporter.stats.get("passed", []))
    failed = len(terminalreporter.stats.get("failed", []))
    error = len(terminalreporter.stats.get("error", []))
    skipped = len(terminalreporter.stats.get("skipped", []))
    # terminalreporter._sessionstarttime 会话开始时间
    duration = time.time() - terminalreporter._sessionstarttime
    deselected = len(terminalreporter.stats.get("deselected", [])) #过滤的用例数
    successful = passed/(total-deselected)*100
    content = "【自动化测试数据显示】\t\n" \
              "用例总数：%s\t\n" \
              "执行用例总数：%s \t\n" \
              "执行SKIP数：%s \t\n" \
              "执行成功数：%s \t\n" \
              "执行失败数：%s \t\n" \
              "执行ERROR数：%s \t\n" \
              "执行成功百分比：%.2f %%  \t\n" \
              "执行时长：%.2f 秒 \t\n" % (total, total-deselected, skipped, passed, failed, error, successful, duration)
    log.info(content)
    with open(BASE_DIR+"result.txt", "w") as fp:
        fp.write("TOTAL=%s" % total+"\n")
        fp.write("PASSED=%s" % passed+"\n")
        fp.write("SKIPPED=%s" % skipped+"\n")
        fp.write("FAILED=%s" % failed+"\n")
        fp.write("ERROR=%s" % error+"\n")
        fp.write("SUCCESSFUL=%.2f%%" % successful+"\n")
        fp.write("TOTAL_TIMES=%.2fs" % duration)



