# 連線到特定網址, 抓取資料
    # 關鍵心法: 盡可能地, 讓程式模仿一個普通使用的樣子

# 解析資料, 取得實際想要的部分
    # if 網站為 JSON 格式資料, 使用 Python 內建的 json 模組即可
    # 大部分為 HTML 格式資料 使用第三方套件 BeautifulSoup 來做解析
        # PIP 套件管理工具: 安裝 Python 時, 就一起安裝在你的電腦裡了
        # 安裝 BeautifulSoup 
            # 指令: pip install beautifulsoup4

# 抓取 網頁原始碼（HTML）
# import urllib.request as req
# url=input("請輸入網址: ")
# with req.urlopen(url) as response:
#     data=response.read().decode("utf-8")
# print(data)

import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html" # input("請輸入網址: ")
# 建立一個 Request 物件, 附加 Request Headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36"
})
with req.urlopen(request) as response: # 用物件打開網址: 看起來比較像正常使用者
    data=response.read().decode("utf-8")
#print(data)

# 解析原始碼，取得每篇文章的標題
import bs4
root=bs4.BeautifulSoup(data, "html.parser") # 讓 BeautifulSoup 協助我們解析 HTML 格式文件
#print(root.title.string)
#titles=root.find("div", class_="title") # 尋找 class_="title" 的 div 標籤
#print(title.a.string)
titles=root.find_all("div", class_="title") # 尋找 class_="title" 所有的 div 標籤
#print(titles)
for title in titles:
    if title.a != None: # 如果標籤包含 a 標籤(沒有被刪除), 印出來
        print(title.a.string)