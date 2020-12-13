# example 1

# import requests
# proxies = {
#     "http": "http://10.10.1.10:3128",
#     "https": "http://10.10.1.10:1080"
# }
# requests.get("http://example.org", proxies=proxies)



# example 2

import urllib.request
import random

url = 'http://www.whatismyip.com.tw'

# 創建 ip 清單，隨機取用 ip
iplist = ['219.223.251.173:3128','203.174.112.13:3128','122.72.18.34:80']
# 創建一個代理 opener
proxy_support = urllib.request.ProxyHandler({'http':iplist[random.randint(0, len(iplist))]})
opener = urllib.request.build_opener(proxy_support)

# 添加瀏覽器偽裝 header
opener.addheaders = [(
    'User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'
)]

# 使用代理 opener 訪問 url
response = opener.open(url)


html = response.read().decode('utf-8')
print(html)