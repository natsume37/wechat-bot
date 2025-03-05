#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：wechat_oa
@File    ：jinrritoutioa
@IDE     ：PyCharm
@Author  ：Martin
@Date    ：2025/3/3 21:17
@Desc    ：文件描述
"""

import requests

res = requests.get(
    "http://m.toutiao.com/list/?tag=__all__&ac=wap&count=20&format=json_raw&as=A17538D54D106FF&cp=585DF0A65F0F1E1&min_behot_time=1482491618")
# print(res.json())
# info_url = requests.get("http://m.toutiao.com/i7477394714241598004/info/")
# print(info_url.text)

data = res.json()
q = data["data"]
for i in q:
    title = i['title']
    abstract = i['abstract']
    print(f"title: {title}  av:{abstract}")