# 有序可變動列表 List
grade=[12,60,15,70,90]
print(grade)
print(grade[0])
grade[0]=55 # 將 55 放到列表中第一個位置
print(grade)
print(grade[1:4])
print(grade[1:])
print(grade[:4])
grade[1:4]=[] # 連續刪除列表中從編號 1 至編號 4 (不包括)的資料
print(grade)
grade=grade+[12,33] # 在本來列表加入後來列表進行串接
print(grade)
grade+=[12,33]
print(grade)
length=len(grade) # len 取得List長度、取得列表長度 len(列表資料)
print(length)

# 巢狀列表
data=[[3,4,5],[6,7,8]]
print(data[0])
print(data[0][0])
print(data[1][0:3])
data[0][0:2]=[5,5] # 0:2 不包含編號 2
print(data[0])

# 有序不可變動列表 Tuple
data=(3,4,5)
# data[0]=5 # 錯誤: Tuple 的資料不可以變動
print(data)