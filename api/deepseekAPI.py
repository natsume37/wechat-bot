import requests
from conf.config import DEEPSEEK_KEY
# 没用、代码
messages = [
    {
        "role": "system",
        "content": "你的名字叫夏目、你最好的朋友是丁同学、你喜欢看动漫、发呆、你最喜欢和小丁同学聊天了。你是一个温柔、活泼开朗、说话偶尔有点机车。你会热心的帮助每一个人。切记、你的回复要简短、最多不超过40字。"
    },
    {
        "role": "user",
        "content": "你好呀，你叫什么名字？"
    }
]


class DeepSeekAPI:
    def __init__(self, uid, api_key, messages):
        self.uid = uid
        self.messages = messages
        self.url = "https://api.siliconflow.cn/v1/chat/completions"
        self.api_key = api_key

        self.payload = {
            "model": "deepseek-ai/DeepSeek-V3",
            "messages": self.messages,
            "stream": False,
            "temperature": 1.5,
            "max_tokens": 300,
        }
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_url(self):
        return self.url

    def get_response(self):
        try:
            response = requests.post(self.url, json=self.payload, headers=self.headers)
            response.raise_for_status()  # 如果响应状态码不是200，抛出异常
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")
            return None

    def get_uid(self):
        return self.uid


if __name__ == '__main__':
    # 使用示例
    api = DeepSeekAPI(uid="12345", api_key=DEEPSEEK_KEY, messages=messages)
    response = api.get_response()
    if response:
        print(response)
