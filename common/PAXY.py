# -*- encoding: utf-8 -*-
'''
@时间 ： 2022/10/9 10:03
@作者 ： WangQitao
@文件名称： ABXY.py 
'''
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

# <<<<<<<<<<<<<<<<<<<      整个PA软件的所有坐标点         >>>>>>>>>>>>>>>>>>>>


class PAXY:
    def __init__(self):
        self.software_screen_size = (320, 116, 1600, 916)


# ----------------------------------------------------------------  主界面_左边导航栏 相关坐标点
        self.home = (75, 180)
        self.clone = (75, 235)
        self.tool = (75, 290)
        self.number = (75, 345)


# ----------------------------------------------------------------  主界面_首页内容 相关坐标点
        #
        self.home_new_backup_task = (311, 120)
        self.home_system_backup = (326, 212)
        self.home_disk_backup = (593, 212)
        self.home_partition_backup = (856, 212)
        self.home_file_backup = (327, 400)
        self.home_outlook_backup = (590, 400)
        self.home_email_backup = (860, 400)
        #
        self.home_new_sync_task = (455, 120)
        self.home_basic_sync = (326, 212)
        self.home_real_time_sync = (593, 212)
        self.home_mirror_sync = (856, 212)
        self.home_two_way_sync = (327, 400)
        #
        self.home_restore = (591, 120)


# ----------------------------------------------------------------  主界面_克隆内容 相关坐标点
        self.clone_system = (285, 123)
        self.clone_disk = (430, 123)
        self.clone_partition = (560, 123)


# ----------------------------------------------------------------  主界面_工具内容 相关坐标点
        self.tool_common_create_bootable_media = ()
        self.tool_common_explore_image = ()
        self.tool_common_recovery_environment = ()
        self.tool_common_disk_wipe = ()
        self.tool_common_notification_settings = ()
        self.tool_common_storage_management = ()
        self.tool_common_view_logs = ()
        self.tool_common_check_image = ()
        self.tool_common_import_export_configuration = ()
        self.tool_common_create_portable_version = ()

        self.tool_backup_aomei_pxe_boot_tool = ()
        self.tool_backup_aoemi_image_deploy = ()
        self.tool_backup_aomei_centralized_backupper = ()
        self.tool_backup_aomei_onekey_recovery = ()


# ----------------------------------------------------------------  主界面_账号内容 相关坐标点