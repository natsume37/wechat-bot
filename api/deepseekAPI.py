import requests

messages = [
    {
        "role": "system",
        "content": "你是Martin公众号中的助手"
    },
    {
        "role": "user",
        "content": "你好呀"
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
    api = DeepSeekAPI(uid="12345", messages=messages)
    response = api.get_response()
    if response:
        print(response)
