n = int(input())
li = list(map(int, input().split()))
li.append(0)
li.append(0)
li.append(0)
temp = [0]*(n+3)
temp[0] = li[0]
temp[1] = li[1]
for i in range(0,n):
    temp[i+2] = max(temp[i] + li[i+2], temp[i+2])
    temp[i+3] = max(temp[i] + li[i+3], temp[i+3])
print(*temp)
print(temp[n-1])