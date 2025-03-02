import pytest
from api import SessionManager, Session
from api import DeepSeekAPI
from conf.config import DEEPSEEK_KEY

@pytest.fixture
def session_manager():
    """Fixture 提供 SessionManager 实例。"""
    api_key = DEEPSEEK_KEY  # 替换为实际的 API 密钥
    return SessionManager(Session, api_key=api_key)


def test_create_session(session_manager):
    """测试创建会话。"""
    session_id = "user_123"
    session = session_manager.build_session(session_id)
    assert session is not None
    assert session.session_id == session_id


def test_add_query_and_reply(session_manager):
    """测试用户提问和助手回复。"""
    session_id = "user_123"
    query = "你好呀，你是谁？"

    # 用户提问
    session_manager.session_query(query, session_id)

    # 获取会话并验证消息
    session = session_manager.get_session(session_id)
    assert len(session.messages) == 2  # 系统提示 + 用户提问
    assert session.messages[-1]["role"] == "user"
    assert session.messages[-1]["content"] == query

    # 调用 DeepSeekAPI 获取助手回复
    reply = session_manager.call_deepseek_api(session_id)
    assert reply is not None

    # 添加助手回复到会话
    session_manager.session_reply(reply, session_id)

    # 验证助手回复是否添加到会话
    session = session_manager.get_session(session_id)
    assert len(session.messages) == 3  # 系统提示 + 用户提问 + 助手回复
    assert session.messages[-1]["role"] == "assistant"
    assert session.messages[-1]["content"] == reply


def test_query_and_reply(session_manager):
    """测试 query_and_reply 方法。"""
    session_id = "user_123"
    query = "你好呀，你是谁？"

    # 用户提问并获取助手回复
    reply = session_manager.query_and_reply(session_id, query)
    assert reply is not None

    # 验证会话消息
    session = session_manager.get_session(session_id)
    assert len(session.messages) == 3  # 系统提示 + 用户提问 + 助手回复
    assert session.messages[-1]["role"] == "assistant"
    assert session.messages[-1]["content"] == reply


def test_clear_session(session_manager):
    """测试清理会话。"""
    session_id = "user_123"
    query = "你好呀，你是谁？"

    # 用户提问并获取助手回复
    session_manager.query_and_reply(session_id, query)

    # 清理会话
    session_manager.clear_session(session_id)

    # 验证会话是否被清理
    session = session_manager.get_session(session_id)
    assert session is None


def test_token_calculation(session_manager):
    """测试 token 计算功能。"""
    session_id = "user_123"
    session = session_manager.build_session(session_id)

    # 添加用户提问
    query = "你好呀，你是谁？"
    session.add_query(query)

    # 计算 token 数量
    token_count = session.calc_tokens()
    assert token_count > 0

    # 清理超出 token 限制的消息
    max_tokens = 13  # 设置一个较小的 token 限制
    session.discard_exceeding(max_tokens)
    assert session.calc_tokens() <= max_tokens