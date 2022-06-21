# 순차탐색이기 때문에 오답이라 볼 수 있음
import sys
n, m = map(int, input().split())
li = list(map(int, sys.stdin.readline().split()))

def cal(li,m):
    for i in range(max(li),0,-1):
        print("i:", i)
        temp = list(map(lambda x:x-i, li))
        print("temp",temp)
        res=0
        for el in temp:
            if(el>0): res+=el
        if(res>=m): return i
    return 0;

res = cal(li, m)
print(res)