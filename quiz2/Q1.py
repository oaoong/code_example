n = int(input())
travelers = sorted(list(map(int, input().split())))
temp = travelers[:]
count = 0
for traveler in travelers:
    if temp.count(traveler) >= traveler:
        count += 1
        for _ in range(traveler): temp.remove(traveler)

print(count)
