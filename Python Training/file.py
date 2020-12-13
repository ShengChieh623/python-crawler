# 開啟檔案
    # 檔案物件=open(檔案路徑,mode=開啟模式)

# 讀取或寫入
    # 讀取模式- r
        # 檔案物件.read()
        # 一次讀取一行
            # for 變數 in 檔案物件
                #從檔案依序讀取每行文字到變數中
        # 讀取 JSON 格式
            # import json
            # 讀取到的資料=json.load(檔案物件)
    # 寫入模式- w
        # 檔案物件.write(字串)
        # 寫入換行符號
            # 檔案物件.write("這是範例文字\n")
        # 寫入 JSON 格式
            # import json
            # json.dump(要寫入的資料, 檔案物件)
    # 讀寫模式- r+

# 關閉檔案
    # 檔案物件.close()

# 最佳實務 with
    # with open(檔案路徑, mode=開啟模式) as 檔案物件:
        # 讀取或寫入檔案的程式
# 以上區塊會自動、安全地關閉檔案
file=open("data.txt", mode="w", encoding="utf-8") # 開啟檔案時, 指定 utf-8 編碼 //中文字
file.write("Hello File\nSecond Line\n中文也可以")
file.close()

with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write("Hello File\nSecond Line\n中文也可以")

with open("data.txt", mode="r", encoding="utf-8") as file:
    data=file.read()
print(data)

with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write("5\n3")

sum=0

with open("data.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        sum+=int(line)
print(sum)