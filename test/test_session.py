#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：wechat_oa
@File    ：test_session
@IDE     ：PyCharm
@Author  ：Martin
@Date    ：2025/3/2 18:59
@Desc    ：文件描述
"""
import pytest
import api


# 测试 Session 类
def test_session_initialization():
    session = api.Session("test_session")
    assert session.session_id == "test_session"
    assert len(session.messages) == 1
    assert session.messages[0]["role"] == "system"
    assert session.messages[0]["content"] == "你是Martin微信公众号的助手"


def test_session_reset():
    session = api.Session("test_session")
    session.add_query("用户提问")
    session.add_reply("助手回复")
    session.reset()
    assert len(session.messages) == 1
    assert session.messages[0]["role"] == "system"
    assert session.messages[0]["content"] == "你是Martin微信公众号的助手"


def test_session_set_system_prompt():
    session = api.Session("test_session")
    session.set_system_prompt("新的系统提示")
    assert session.system_prompt == "新的系统提示"
    assert len(session.messages) == 1
    assert session.messages[0]["role"] == "system"
    assert session.messages[0]["content"] == "新的系统提示"


def test_session_add_query():
    session = api.Session("test_session")
    session.add_query("用户提问")
    assert len(session.messages) == 2
    assert session.messages[-1]["role"] == "user"
    assert session.messages[-1]["content"] == "用户提问"


def test_session_add_reply():
    session = api.Session("test_session")
    session.add_reply("助手回复")
    assert len(session.messages) == 2
    assert session.messages[-1]["role"] == "assistant"
    assert session.messages[-1]["content"] == "助手回复"


def test_session_calc_tokens():
    session = api.Session("test_session")
    session.add_query("用户提问")
    session.add_reply("助手回复")
    tokens = session.calc_tokens()
    assert tokens > 0


def test_session_discard_exceeding():
    session = api.Session("test_session")
    session.add_query("用户提问")
    session.add_reply("助手回复")
    max_tokens = 13  # 假设最大 token 数量为 10
    tokens = session.discard_exceeding(max_tokens)
    assert tokens <= max_tokens
    assert len(session.messages) >= 1


# 测试 SessionManager 类
def test_session_manager_initialization():
    session_manager = api.SessionManager(api.Session)
    assert session_manager.session_class == api.Session
    assert session_manager.expires_in_seconds is None
    assert len(session_manager.sessions) == 0


def test_session_manager_build_session():
    session_manager = api.SessionManager(api.Session)
    session = session_manager.build_session("test_session")
    assert session.session_id == "test_session"
    assert len(session.messages) == 1
    assert session.messages[0]["role"] == "system"
    assert session.messages[0]["content"] == "你是Martin微信公众号的助手"


def test_session_manager_build_session_with_system_prompt():
    session_manager = api.SessionManager(api.Session)
    session = session_manager.build_session("test_session", "新的系统提示")
    assert session.system_prompt == "新的系统提示"
    assert len(session.messages) == 1
    assert session.messages[0]["role"] == "system"
    assert session.messages[0]["content"] == "新的系统提示"


def test_session_manager_session_query():
    session_manager = api.SessionManager(api.Session)
    session = session_manager.session_query("用户提问", "test_session")
    assert len(session.messages) == 2
    assert session.messages[-1]["role"] == "user"
    assert session.messages[-1]["content"] == "用户提问"


def test_session_manager_session_reply():
    session_manager = api.SessionManager(api.Session)
    session = session_manager.session_reply("助手回复", "test_session")
    assert len(session.messages) == 2
    assert session.messages[-1]["role"] == "assistant"
    assert session.messages[-1]["content"] == "助手回复"


def test_session_manager_clear_session():
    session_manager = api.SessionManager(api.Session)
    session_manager.build_session("test_session")
    session_manager.clear_session("test_session")
    assert "test_session" not in session_manager.sessions


def test_session_manager_clear_all_sessions():
    session_manager = api.SessionManager(api.Session)
    session_manager.build_session("test_session1")
    session_manager.build_session("test_session2")
    session_manager.clear_all_sessions()
    assert len(session_manager.sessions) == 0


def test_session_manager_get_session():
    session_manager = api.SessionManager(api.Session)
    session_manager.build_session("test_session")
    session = session_manager.get_session("test_session")
    assert session.session_id == "test_session"
    assert len(session.messages) == 1
    assert session.messages[0]["role"] == "system"
    assert session.messages[0]["content"] == "你是Martin微信公众号的助手"


def test_session_manager_get_nonexistent_session():
    session_manager = api.SessionManager(api.Session)
    session = session_manager.get_session("nonexistent_session")
    assert session is None
