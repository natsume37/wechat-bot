import requests
import json
from conf.config import DEEPSEEK_KEY
from openai import OpenAI


class DeepSeekAPI:
    # Please install OpenAI SDK first: `pip3 install openai`

    def __init__(self, deepseek):
        self.deepseek_key = deepseek

    def push(self):
        client = OpenAI(api_key=self.deepseek_key, base_url="https://api.deepseek.com/v1")

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你现在是Martin的公众号助手"},
                {"role": "user", "content": "你好，你是谁？"},
            ],
            stream=False
        )

        print(response.choices[0].message.content)


# 使用示例
if __name__ == "__main__":
    test = DeepSeekAPI(DEEPSEEK_KEY)
    test.push()
