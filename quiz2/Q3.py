s = input()
count = 0
temp = s[0]
for i in range(1, len(s)):
    if temp != s[i]:
        count += 1
    temp = s[i]

print(count-1)
