import requests

res = requests.get('https://orz.ai/dailynews/?platform=baidu')
print(res.text)
