# coding=utf-8
import requests

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'

# 使用resquests.get方法读取网页数据
req = requests.get(json_url)
with open('btc_close_2017_requests.json', 'w') as f:
    f.write(req.text)
    
file_requests = req.json()
