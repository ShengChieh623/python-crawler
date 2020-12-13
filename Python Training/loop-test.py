n=0
while n<100: # 100以內的雙乘數
    for x in range(n):
        if x*x==n:
            print("有平方根的整數: ",n,"平方根為: ",x)
            print(x, "*", x, "=", n)
            break
    n+=1