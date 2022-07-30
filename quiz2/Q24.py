n = int(input())
loc = sorted(list(map(int, input().split())))
far = [0]*len(loc)
i=0
for house in loc:
    res = 0
    for other in loc:
        res += abs(house-other)
    far[i] = res
    i += 1
ans = loc[far.index(min(far))]
print(ans)