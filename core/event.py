#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：wechat_oa
@File    ：event
@IDE     ：PyCharm
@Author  ：Martin
@Date    ：2025/2/26 19:34
@Desc    ：事件函数
"""
import werobot
from conf.config import *
from api1.deepseek import DeepSeekAPI

robot = werobot.WeRoBot(token='martin')
config = configparser.ConfigParser.read("./config.ini")

robot.config["APP_ID"] = WECHAT_APP_ID
robot.config["APP_SECRET"] = WECHAT_APPSECRET


@robot.subscribe
def subscribe(message):
    """
    :param message:
    :return:
    新关注回复函数
    """
    return '欢迎关注Martin的成长日记！'


def deepseek_response(deepseek_key):
    response = DeepSeekAPI(deepseek_key)
    return response.generate_text()


@robot.text
def echo(message, deepseek_key=None):
    """
    文本类型回复函数，接入deepseek
    :param deepseek_key:
    :param message:
    :return:
    """
    return deepseek_response(deepseek_key)


@robot.unknown_event
def none(message):
    """
    未知类型
    :return:
    """
    return "目前Martin正在学习中！请换个问题吧！"


@robot.image
def img(message):
    """
    图片类型
    :return:
    """
    return "目前暂不支持图片幺，因为技术菜！请发送文本信息"


# 点击事件
@robot.click
def handle_click(event):
    """
    菜单点击事件
    :param event:
    :return:
    """
    # 点击新闻按钮事件
    if event.key == 'V1001_TODAY_NEWS':
        return '你点击了菜单1'
    # 点击每日一言事件
    elif event.key == 'V1001_TODAY_ENGLISH':
        return '你点击了菜单2'
    # 点击点赞按钮
    elif event.key == 'V1001_GOOD':
        return '感谢你的认可'
    # 未知菜单事件
    else:
        return '未知菜单'



# 处理文本消息
@robot.text
def echo(message):
    """
    获取用户的openID
    :param message:
    :return:
    """
    return message.source
