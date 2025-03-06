#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：wechat_oa
@File    ：core
@IDE     ：PyCharm
@Author  ：Martin
@Date    ：2025/2/26 16:53
@Desc    ：文件描述
"""
from core.event import robot

# 自定义菜单
client = robot.client
client.create_menu({
    "button": [
        {
            "type": "click",
            "name": "今日新闻",
            "key": "V1001_TODAY_NEWS"
        },
        {
            "type": "click",
            "name": "每日一言",
            "key": "V1001_TODAY_ONESEY"
        },
        {
            "name": "更多",
            "sub_button": [
                {
                    "type": "view",
                    "name": "搜索恩师",
                    "url": "https://search.bilibili.com/all?vt=49140046&keyword=%E5%B0%8F%E9%A3%9E%E6%9C%89%E7%82%B9%E4%B8%9C%E8%A5%BF&from_source=webtop_search&spm_id_from=333.1007&search_source=5"
                },
                {
                    "type": "view",
                    "name": "视频",
                    "url": "http://v.qq.com/"
                },
                {
                    "type": "click",
                    "name": "赞一下我们",
                    "key": "V1001_GOOD"
                }
            ]
        }
    ]}
)

# 获取用户ID

# import api
# if __name__ == '__main__':
#     # 调用新闻接口
