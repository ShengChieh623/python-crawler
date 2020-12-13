# 集合的運算
s1={3,4,5}
print(3 in s1) # 用 in 判斷 3 是否在 s1 集合中
print(3 not in s1) # 用 not in 判斷 3 是否不在 s1 集合中
s2={4,5,6,7}
s3=s1&s2 # 交集: & 取兩個集合中，相同的資料
print(s3)
s3=s1|s2 # 聯集: | 取兩個集合中的所有資料，但不重複取
print(s3) 
s3=s1-s2 # 差集: - 從 s1 中減去 s2 重疊的部分
print(s3)
s3=s2-s1
print(s3)
s3=s1^s2 # 反交集: ^ 取兩個集合中，不重疊的部分
print(s3)

# 拆解字串為集合
s=set("Hello") # set(字串): 會將字串自動拆解成集合，且不重複
print(s)
print("H" in s)

# 字典的運算: key-value 配對
dic={"apple":"蘋果","bug":"蟲蟲"}
print(dic["apple"])
dic["apple"]="小蘋果"
print(dic["apple"])
print("apple" in dic) # 判斷的對象為 key 是否存在，不會判斷 value
print("apple" not in dic)
print(dic)
del dic["apple"] # del 刪除字典中的鍵值對 (key-value pair)
print(dic)

# 用列表資料產生字典
dic={i:i*2 for i in [3,4,5]} # 將列表[3,4,5]為 i 轉換為鍵值對 i*2 產生字典
print(dic)