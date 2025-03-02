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

# 可选：定义 __all__，明确暴露的接口
__all__ = [
    "DeepSeekAPI",
    "NewsApi",
]
