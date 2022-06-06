n = int(input())
li = [list(map(str, input().split())) for _ in range(n)]
li = sorted(li, key = lambda x:int(x[1]))
for el in li: print(el[0], end=" ")