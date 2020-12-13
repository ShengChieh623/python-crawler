def __init__(self):
        self.cookies = requests.cookies.RequestsCookieJar()

def go(self, url, method, post_data):
        response = requests.request(method, url
                                    , data=post_data
                                    , headers=info.headers
                                    , cookies=self.cookies) # 傳遞 cookie

        self.cookies.update(response.cookies) # 保存 cookie

# 用於同一個網址的訪問維持 cookies

# session 存在伺服端，可以跨請求保存參數，但須帶上第一次產生的cookie
# cookies 存在用戶端

import requests
from requests.cookies import RequestsCookieJar
cookie_jar = RequestsCookieJar()
cookie_jar.set("BAIDUID", "4EDT7A5263775F7E0A4B&F330724:FG=1", domain="baidu.com")
response = requests.get("https://fanyi.baidu.com/", cookies=cookie_jar)
