#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：wechat_oa
@File    ：app
@IDE     ：PyCharm
@Author  ：Martin
@Date    ：2025/2/26 16:52
@Desc    ：文件描述
"""
from core.core import *

if __name__ == '__main__':
    # 让服务器监听在 0.0.0.0:80
    robot.config['HOST'] = '0.0.0.0'
    robot.config['PORT'] = 80
    robot.run()
