#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project    ：wecha_oa 
@File       ：server_push.py
@IDE        ：PyCharm 
@Author     ：Martin
@Date       ：2025/2/26 12:05 
@description；server酱推送服务
"""
import configparser
import json

import requests

config = configparser.ConfigParser()
config.read('./conf.ini')
senurl = config.get('server', 'url')

print(senurl)


def push_msg(url, msg_push):
    msg_json = {
        "title": "每日新闻",
        "desp": f"{msg_push}",
        "channel": "9",
    }
    requests.post(url=url, params=msg_json)


push_msg(senurl, "测试文件")
