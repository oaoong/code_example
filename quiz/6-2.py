n = int(input())
li=[int(input()) for _ in range(n)]
print(*sorted(li)[::-1], sep=" ")
    