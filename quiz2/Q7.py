n = input()
pre = 0
post = 0
for i in range(len(n)//2):
    pre += int(n[i])
    post += int(n[len(n)-i-1])

print('LUCKY') if (pre == post) else print('READY')