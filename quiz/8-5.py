n, m = map(int, input().split())
li = [int(input()) for _ in range(n)]
li.sort(reverse=True)
temp=[10001]*(m+1)*li[0]
for el in li:
    temp[el] = 1
for i in range(1,m+1):
    a = []
    for el in li:
        a.append(temp[i-el])
    if min(a) != 10001: temp[i] = min(a) + 1

print(-1) if temp[m] == 10001 else print(temp[m])