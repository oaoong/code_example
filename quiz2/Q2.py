s = input()
res = int(s[0])
for i in range(1, len(s)):
    if res <= 1 or int(s[i]) <= 1:
        res += int(s[i])
    else:
        res *= int(s[i])

print(res)
