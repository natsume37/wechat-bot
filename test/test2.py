import requests
import json


class DeepSeekAPI:
    def __init__(self, api_key, base_url="https://api.deepseek.com/v1"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def _make_request(self, endpoint, method="GET", data=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, headers=self.headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

    def get_models(self):
        """获取可用的模型列表"""
        return self._make_request("models")

    def generate_text(self, model, prompt, max_tokens=50, temperature=0.7):
        """生成文本"""
        data = {
            "model": model,
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature
        }
        return self._make_request("generate", method="POST", data=data)

    def get_model_info(self, model_id):
        """获取特定模型的详细信息"""
        return self._make_request(f"models/{model_id}")


# 使用示例
if __name__ == "__main__":
    api_key = "sk-d29649ae24f94bff94aad53206631d8d"
    deepseek = DeepSeekAPI(api_key)

    # 获取模型列表
    models = deepseek.get_models()
    print("Available Models:", models)

    # 生成文本
    model = "deepseek-chat"  # 替换为实际的模型ID
    prompt = "Once upon a time"
    generated_text = deepseek.generate_text(model, prompt, max_tokens=100)
    print("Generated Text:", generated_text)

    # 获取模型信息
    model_info = deepseek.get_model_info(model)
    print("Model Info:", model_info)
