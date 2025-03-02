#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：wechat_oa
@File    ：session_manage.py
@IDE     ：PyCharm
@Author  ：Martin
@Date    ：2025/3/1 20:47
@Desc    ：会话管理
"""
from conf.setting import logger2
from typing import Dict, Optional, Type, List
from collections import defaultdict
import tiktoken  # 用于计算 token 数量


class SessionManager:
    """
    会话管理器，用于管理多个会话（Session 实例）。
    """

    def __init__(self, session_class: Type['Session'], expires_in_seconds: Optional[int] = None):
        """
        初始化 SessionManager。

        :param session_class: 会话类（必须是 Session 或其子类）。
        :param expires_in_seconds: 会话过期时间（秒），如果为 None，则会话不会过期。
        """
        self.session_class = session_class
        self.sessions: Dict[str, 'Session'] = defaultdict(lambda: None)  # 存储会话的字典
        self.expires_in_seconds = expires_in_seconds

    def build_session(self, session_id: str, system_prompt: Optional[str] = None) -> 'Session':
        """
        创建或获取一个会话。

        :param session_id: 会话的唯一标识。
        :param system_prompt: 系统提示，如果提供，会更新会话的系统提示并重置会话。
        :return: Session 实例。
        """
        if session_id not in self.sessions or self.sessions[session_id] is None:
            # 如果会话不存在，创建一个新的会话
            self.sessions[session_id] = self.session_class(session_id)
            logger2.debug(f"创建新会话: session_id={session_id}")

        session = self.sessions[session_id]

        if system_prompt is not None:
            # 如果提供了 system_prompt，更新并重置会话
            session.set_system_prompt(system_prompt)
            logger2.debug(f"更新系统提示并重置会话: session_id={session_id}")

        return session

    def session_query(self, query: str, session_id: str) -> 'Session':
        """
        将用户提问添加到会话中。

        :param query: 用户提问内容。
        :param session_id: 会话的唯一标识。
        :return: 更新后的 Session 实例。
        """
        session = self.build_session(session_id)
        session.add_query(query)
        logger2.debug(f"添加用户提问到会话: session_id={session_id}, query={query}")
        return session

    def session_reply(self, reply: str, session_id: str) -> 'Session':
        """
        将助手回复添加到会话中。

        :param reply: 助手回复内容。
        :param session_id: 会话的唯一标识。
        :return: 更新后的 Session 实例。
        """
        session = self.build_session(session_id)
        session.add_reply(reply)
        logger2.debug(f"添加助手回复到会话: session_id={session_id}, reply={reply}")
        return session

    def clear_session(self, session_id: str):
        """
        清理指定会话。

        :param session_id: 会话的唯一标识。
        """
        if session_id in self.sessions:
            del self.sessions[session_id]
            logger2.debug(f"清理会话: session_id={session_id}")

    def clear_all_sessions(self):
        """
        清理所有会话。
        """
        self.sessions.clear()
        logger2.debug("清理所有会话")

    def get_session(self, session_id: str) -> Optional['Session']:
        """
        获取指定会话。

        :param session_id: 会话的唯一标识。
        :return: Session 实例，如果会话不存在则返回 None。
        """
        return self.sessions.get(session_id)


class Session:
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.messages: List[Dict[str, str]] = []
        self.reset()

    def reset(self):
        """重置会话，只保留系统提示。"""
        self.messages = [{"role": "system", "content": "你是Martin微信公众号的助手"}]

    def set_system_prompt(self, system_prompt: str):
        """设置系统提示并重置会话。"""
        self.system_prompt = system_prompt
        self.reset()

    def add_query(self, query: str):
        """添加用户提问到会话中。"""
        self.messages.append({"role": "user", "content": query})

    def add_reply(self, reply: str):
        """添加助手回复到会话中。"""
        self.messages.append({"role": "assistant", "content": reply})

    def discard_exceeding(self, max_tokens: int) -> int:
        """
        清理超出 token 限制的早期消息。

        :param max_tokens: 允许的最大 token 数量。
        :return: 清理后的总 token 数量。
        """
        while self.calc_tokens() > max_tokens and len(self.messages) > 1:
            # 保留系统提示，清理最早的用户或助手消息
            self.messages.pop(1)
        return self.calc_tokens()

    def calc_tokens(self) -> int:
        """
        计算当前会话中所有消息的总 token 数量。

        :return: 总 token 数量。
        """
        encoding = tiktoken.get_encoding("cl100k_base")  # 使用 GPT-3.5/GPT-4 的编码
        total_tokens = 0
        for message in self.messages:
            total_tokens += len(encoding.encode(message["content"]))
        return total_tokens


# 示例使用
if __name__ == '__main__':
    # 初始化 SessionManager
    session_manager = SessionManager(Session)

    # 创建或获取一个会话
    session_id = "user_123"
    session = session_manager.build_session(session_id)

    # 添加用户提问
    session_manager.session_query("你好呀，你是谁？", session_id)

    # 添加助手回复
    session_manager.session_reply("你好！我是Martin微信公众号的助手。", session_id)

    # 打印当前会话的消息
    print("当前会话消息:", session.messages)

    # 清理超出 token 限制的消息
    max_tokens = 50  # 假设最大 token 数量为 50
    session.discard_exceeding(max_tokens)
    print("清理后的会话消息:", session.messages)

    # 清理会话
    session_manager.clear_session(session_id)
    print(f"会话 {session_id} 已清理。")