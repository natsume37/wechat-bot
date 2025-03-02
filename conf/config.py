#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：wechat_oa
@File    ：config
@IDE     ：PyCharm
@Author  ：Martin
@Date    ：2025/2/26 17:27
@Desc    ：配置信息提取
"""
import configparser
import os
import sys
# 获取项目根目录
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 构建配置文件的绝对路径
config_path = os.path.join(project_root, 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)
WECHAT_APP_ID = config.get('wechat', 'AppID')
WECHAT_APPSECRET = config.get('wechat', 'AppSecret')
DEEPSEEK_KEY = config.get('deepseek', 'DeepSeekKey')
NEWS_KEY = config.get('newsapi', 'news-key')


