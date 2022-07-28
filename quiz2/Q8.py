import re
s = input()
res = 0
alpha = re.findall('[a-zA-z]', s)
nums = re.findall('\d', s)
print(*sorted(alpha), sep="", end="")
for num in nums:
    res += int(num)
if res!=0: print(res)