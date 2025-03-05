#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：wechat_oa
@File    ：news
@IDE     ：PyCharm
@Author  ：Martin
@Date    ：2025/2/28 23:10
@Desc    ：新闻接口
"""

from conf.config import NEWS_KEY

import api

# 实例化并调用
if __name__ == '__main__':
    news_api = api.NewsApi(NEWS_KEY)
    hot_news_data = news_api.hot_news()
    if hot_news_data:
        print(hot_news_data)
