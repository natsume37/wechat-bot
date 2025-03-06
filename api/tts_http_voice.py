# coding=utf-8

'''
requires Python 3.6 or later
pip install requests
'''
import base64
import json
import uuid
import requests

from conf.config import config, voice_path
from conf.setting import logger2


class TextToSpeech:

    def __init__(self, text_to_voice):
        self.text_to_voice = text_to_voice
        self.app_id = config.get('huosan', 'AppID')
        self.access_token = config.get('huosan', 'AccessToken')
        self.secret_key = config.get('huosan', 'SecretKey')
        self.voice_id = config.get('huosan', 'VoiceID')
        self.cluster = "volcano_icl"
        self.host = "openspeech.bytedance.com"
        self.api_url = f"https://{self.host}/api/v1/tts"
        self.header = {"Authorization": f"Bearer;{self.access_token}"}

    def generate_speech(self, output_file=voice_path):
        request_json = {
            "app": {
                "appid": self.app_id,
                "token": self.access_token,
                "cluster": self.cluster
            },
            "user": {
                "uid": "388808087185088"
            },
            "audio": {
                "voice_type": self.voice_id,
                "encoding": "mp3",
                "speed_ratio": 1.0,
                "volume_ratio": 1.0,
                "pitch_ratio": 1.0,
            },
            "request": {
                "reqid": str(uuid.uuid4()),
                "text": self.text_to_voice,
                "text_type": "plain",
                "operation": "query",
                "with_frontend": 1,
                "frontend_type": "unitTson"
            }
        }

        try:
            resp = requests.post(self.api_url, json.dumps(request_json), headers=self.header)
            logger2.debug(f"resp body: \n{resp.json()}")
            if "data" in resp.json():
                data = resp.json()["data"]
                with open(output_file, "wb") as file_to_save:
                    file_to_save.write(base64.b64decode(data))
                logger2.debug(f"Speech saved to {output_file}")
                return True
            else:
                logger2.debug("Failed to generate speech.")
                return None
        except Exception as e:
            logger2.debug(f"An error occurred: {e}")
            return None


if __name__ == '__main__':
    # 示例用法
    text_to_voice = "你好，这是一个测试文本。"
    tts = TextToSpeech(text_to_voice)
    tts.generate_speech("test_submit.mp3")
