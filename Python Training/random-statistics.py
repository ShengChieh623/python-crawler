# 隨機模組
import random
# 隨機選取
# data=random.choice([5,4,7,10,15])
# data=random.sample([5,4,7,10,15],3)
# print(data)
# 隨機調換順序
# data=[1,5,7,8,10,20]
# random.shuffle(data)
# print(data)
# 隨機取得亂數
# data=random.random() # 0 ~ 1 之間的隨機亂數 # data=random.uniform(0.0, 1.0)
# print(data)
# 取得常態分配亂數
# data=random.normalvariate(100, 10) # 平均數 100, 標準差 10, 得到的資料多數在 90 ~ 110 之間
# print(data)

# 統計模組
import statistics as stat
data=stat.median([1,2,3,5,7,10,100]) # 中位數
print(data)
data=stat.stdev([1,2,3,5,7,10,100]) # 標準差
print(data)

# 平均數、中位數、標準差、常態分配