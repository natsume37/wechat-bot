from openai import OpenAI
from conf.setting import logger2

class DeepSeekAPI:
    def __init__(self, deepseek):
        self.deepseek_key = deepseek

    def generate_text(self):
        try:
            client = OpenAI(api_key=self.deepseek_key, base_url="https://api.deepseek.com/v1")

            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "你现在是Martin的公众号助手"},
                    {"role": "user", "content": "你好，你是谁？"},
                ],
                stream=False
            )

            return response.choices[0].message.content
        except Exception as e:
            logger2.error(f"DeepSeekAPI 调用失败: {e}")
            return "服务暂时不可用，请稍后再试。"
