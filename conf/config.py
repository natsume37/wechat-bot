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

config = configparser.ConfigParser()
config.read("../config.ini")
WECHAT_APP_ID = config.get('wechat', 'AppID')
WECHAT_APPSECRET = config.get('wechat', 'AppSecret')
DEEPSEEK_KEY = config.get('deepseek', 'DeepSeekKey')
