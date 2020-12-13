# session 存在伺服端，可以跨請求保存參數，但須帶上第一次產生的cookie
# cookies 存在用戶端

import requests

headers = {  
    "content-type":"application/x-www-form-urlencoded;charset=UTF-8",
    "User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6)"
}

#設置一個會話 session 對象 s
s = requests.session()
resp = s.get('https://www.baidu.com/s?wd=python', headers=headers)
 # 列印請求頭和 cookies
 print(resp.request.headers) print(resp.cookies) 
 # 利用s再訪問一次
 resp = s.get('https://www.baidu.com/s?wd=python', headers=headers)
 # 請求頭已保持首次請求後產生的 cookie
 print(resp.request.headers) print(resp.cookies)