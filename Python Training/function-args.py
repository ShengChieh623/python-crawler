# 無限/不定 參數資料
def avg(*ns):
    sum=0
    for n in ns:
        sum+=n
    nl = sum/len(ns)
    print(nl)
    return nl
avg(1,2,3,4,5)
avg(1,-2,3,-4,5)