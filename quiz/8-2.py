n = int(input())
li = [30001]*(n+1)*5
li[1] = 0
for i in range(1,n):
    li[i*5] = min(li[i]+1, li[i*5])
    li[i*3] = min(li[i]+1, li[i*3])
    li[i*2] = min(li[i]+1, li[i*2])
    li[i+1] = min(li[i]+1, li[i+1])

print(li[n])