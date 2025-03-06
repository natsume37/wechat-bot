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
from werobot.replies import VoiceReply
from typing import Optional
from api import SessionManager, Session, ask_deepseek, TextToSpeech
from conf.config import *
import api
from conf.setting import logger2

robot = werobot.WeRoBot(token='martin')
# config = configparser.ConfigParser.read(config_path)

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


# deepseek会话处理
# def deepseek_response(openID, api_key, msg):
#     # 会话管理
#     response = api.DeepSeekAPI(openID, )
#     return response.get_response()


@robot.text
def echo(message):
    """
    文本类型回复函数，接入deepseek
    :param deepseek_key:
    :param message:
    :return:
    """
    # uid = message.source
    # return deepseek_response(deepseek_key)
    # 暂时仅支持语音
    try:
        recognition = message.recognition
        # deepseek回复
        deepseek_response = replay_form_deepseek(message.source, recognition)
        return deepseek_response
    except:
        return "网络出现问题、请稍后再试吧。"


def replay_form_deepseek(session_id, user_query):
    """
    整合接口、让代码简洁一点
    :return: 助手的回复内容，如果请求失败则返回 None。
    """
    api_key = DEEPSEEK_KEY  # 替换为实际的 API 密钥
    session_manager = SessionManager(Session, api_key=api_key)

    # 创建或获取一个会话
    session_manager.build_session(session_id)

    # 用户提问并获取助手的回复
    reply = ask_deepseek(session_manager, session_id, user_query)

    if reply:
        logger2.debug(f"助手的回复: {reply}")
        return reply
    else:
        logger2.debug("请求失败，请检查日志。")
        return "请求失败，请检查日志。"


# 语音回复
@robot.voice
def replay_voice(message):
    try:
        # 获取微信翻译好的语音文本、不确定真的假的、文档是这样写的
        recognition = message.recognition
        # deepseek回复
        deepseek_response = replay_form_deepseek(message.source, recognition)
        # 语音合成
        tts_voice = TextToSpeech(deepseek_response).generate_speech(voice_path)
        logger2.debug("语音合成成功")
        if tts_voice:
            # logger2.debug(tts_voice)
            # logger2.debug("上传ID")
            # 上传语音文件并获取 MediaId
            with open(voice_path, 'rb') as f:
                media_info = robot.client.upload_media("voice", f)
                media_id = media_info["media_id"]
            # logger2.debug("音频id上传成功")
            # 返回语音回复
            return VoiceReply(message, media_id=media_id)
    except Exception as e:
        logger2.info(e)
        return "语音回复失败"
#
# @robot.unknown_event
# def none(message):
#     """
#     未知类型
#     :return:
#     """
#     return "目前Martin正在学习中！请换个问题吧！"
#
#
# @robot.image
# def img(message):
#     """
#     图片类型
#     :return:
#     """
#     return "目前暂不支持图片幺，因为技术菜！请发送文本信息"
#
#
# def click_news(new_key):
#     """
#      # 新闻内存排版重组
#     """
#     pass
#
#
# # 点击事件
# @robot.click
# def handle_click(event):
#     """
#     菜单点击事件
#     :param event:
#     :return:
#     """
#     # 点击新闻按钮事件
#     if event.key == 'V1001_TODAY_NEWS':
#         news = api.NewsApi(NEWS_KEY)
#         return '你点击了菜单1'
#     # 点击每日一言事件
#     elif event.key == 'V1001_TODAY_ENGLISH':
#         return '你点击了菜单2'
#     # 点击点赞按钮
#     elif event.key == 'V1001_GOOD':
#         return '感谢你的认可'
#     # 未知菜单事件
#     else:
#         return '未知菜单'
#
#
# # 处理文本消息
# @robot.text
# def echo(message):
#     """
#     获取用户的openID
#     :param message:
#     :return:
#     """
#     return message.source
