#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：wechat_oa
@File    ：__init__.py
@IDE     ：PyCharm
@Author  ：Martin
@Date    ：2025/3/1 18:05
@Desc    ：文件描述
"""
# api/__init__.py

# 从各个模块中导入功能
from .deepseekAPI import DeepSeekAPI
from .news import NewsApi
from .session_manage import Session, SessionManager, ask_deepseek
from .tts_http_voice import TextToSpeech

__all__ = [
    "DeepSeekAPI",
    "NewsApi",
    "Session",
    "SessionManager",
    "TextToSpeech",
    "ask_deepseek"
]
