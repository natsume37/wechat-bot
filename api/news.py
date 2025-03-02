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
import requests

from conf.setting import logger2


class NewsApi:
    """
    新闻API调用接口
    """

    def __init__(self, news_key):
        """
        初始化方法
        :param news_key: API 密钥
        """
        self.news_key = news_key

    def hot_news(self):
        """
        获取热点新闻
        :return: 返回热点新闻的 JSON 数据，如果请求失败则返回 None
        """
        try:
            res = requests.get(url=f'https://whyta.cn/api/tx/bulletin?key={self.news_key}')
            res.raise_for_status()  # 检查请求是否成功
            return res.json()
        except requests.exceptions.RequestException as e:
            logger2.debug(f"请求失败: {e}")
            return None

    def everyday_english(self):
        """
        获取每日英语
        :return: 返回每日英语的 JSON 数据，如果请求失败则返回 None
        """
        try:
            res = requests.get(url=f"https://whyta.cn/api/tx/everyday?key={self.news_key}")
            res.raise_for_status()  # 检查请求是否成功
            return res.json()
        except requests.exceptions.RequestException as e:
            logger2.debug(f"请求失败: {e}")
            return None

#
# # 实例化并调用\
# if __name__ == '__main__':
#     news_api = NewsApi(NEWS_KEY)
#     hot_news_data = news_api.hot_news()
#     if hot_news_data:
#         print(hot_news_data)
