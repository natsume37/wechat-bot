import api
from conf.config import DEEPSEEK_KEY

messages = [
    {"role": "system", "content": "你是Martin公众号中的助手"},
    {"role": "user", "content": "你好呀，你还谁？"}
]

# 使用示例
api = api.DeepSeekAPI(uid="12345", api_key=DEEPSEEK_KEY, messages=messages)
response = api.get_response()
if response:
    print(response)
