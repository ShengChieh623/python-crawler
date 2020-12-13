# pip3 install fake_useragent
# pip3 install pandas

keyword = input("請輸入關鍵字: ")

import requests
import json
from fake_useragent import UserAgent
import pandas as pd
import time

def Suggest(query):
    query.replace(" ", "+")
    hl="zh-TW"
    gl="tw"
    url = "http://suggestqueries.google.com/complete/search?output=chrome&q={}&hl={}&gl={}".format(query,hl,gl)
    ua = UserAgent() 
    headers = {"user-agent": ua.random}

    response = requests.get(url, headers=headers, verify=True)
    results = json.loads(response.text)
    return results

def word_group(results):
    data = []
    for word in results[1]: # keyword 的建議相關字，逐一執行迴圈 
        k = Suggest(word)[0] # 每一個字執行一次 Suggest 並存至 k ，共 7 次
        deep_words = Suggest(word)[1] # 每一個 k 的 7 個序列
        suggestRelevance = Suggest(word)[4].get('google:suggestrelevance') # 每一個 k 的 7 個序列的關聯分數

        i=0
        for deep_word in deep_words: # 每一個 k 的 7 個序列逐一執行
            group = [results[0], suggestRelevance[i], k, deep_word]
            data.append(group)
            i+=1

    return data

def get_autocomp_kws(query):
    results = Suggest(query)
    data = word_group(results)
    return data

data = []

google_suggest = get_autocomp_kws(keyword)
data = data + google_suggest
print('Searching [{}] ...'.format(keyword))
time.sleep(2)

print("Search is Done.")
df = pd.DataFrame(data, columns=['關鍵字', '分數', '預測字', '預測字的預測字'])
fileName = keyword+'.csv'
df.to_csv(fileName, index=False, header=True, encoding='utf-16')