# 數字運算
x=3+6
print(x)
x=3-6
print(x)
x=3/6 # 小數除法，看小數點
print(x)
x=3//6 # 整數除法，不看小數點
print(x)
x=2**3 # 2的3次方
print(x)
x=2**0.5 # **0.5開根號
print(x)
x=7%3 # 餘數
print(x)
x=x+1 # 將變數中的數字 +1
print(x)
x+=1 # 同上簡寫法
print(x)
x-=1
print(x)
x*=2
print(x)

# 字串運算
s="Hello"
print(s)
s='Hello' # 與上述字串相同
print(s)
s="Hello\"" # \ 跳脫字串，有時字串需要"
print(s)
s="Hello"+" World" # 字串串接
print(s)
s="Hello" " World" # python 也可以用 space 替代 + 字串串接
print(s)
s="Hello\nWorld" # \n 換行
print(s)
s="""Hello

World""" # 三個"可以做大段落字串
print(s)
s="Hello "*3+"World" # 字串可以乘法重複出現
print(s)

# 字串會對內部的字元編號(索引)，從 0 開始算起
s="Hello"
print(s[0])
print(s[1:4]) # 可以用開始:至結束，快速取的子字串
print(s[1:])
print(s[:4])