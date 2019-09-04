# coding=utf-8

from __future__ import (absolute_import, division, print_function, unicode_literals)

try:
    # python 2.x
    from urllib2 import urlopen
except ImportError:
    # python 3.x
    from urllib.request import urlopen

import json
import ssl


json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"
response = urlopen(json_url, context=ssl._create_unverified_context())

#读取数据
req = response.read()

#将数据写入到文件
with open('btc_close_2017_urllib.json', 'wb') as f:
    f.write(req)

#加载json格式
file_urllib = json.loads(req)

print(file_urllib)
