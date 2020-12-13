# while 迴圈
# 1+2+3+...+10
n=1
sum=0 # 紀錄累加結果
while n<=10:
    sum+=n
    n+=1
print(sum)

# for 迴圈
sum2=0
for x in [3,5,1]:
    print(x)
for x in "Hello":
    print(x)
for x in range(5):
    print(x)
for x in range(5,10):
    print(x)
for x in range(1,11):
    sum2+=x
print(sum2)