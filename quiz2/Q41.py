n, m = map(int, input().split())
parents = [i for i in range(n+1)]
roads = [[] for _ in range(n+1)]

def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_parent(parents, x, y):
    a = find_parent(parents, x)
    b = find_parent(parents, y)

    if (a < b):
        parents[b] = a
    else:
        parents[a] = b


for i in range(n):
    li = list(map(int, input().split()))
    for j in range(n):
        if li[j] == 1:
            union_parent(parents, i+1, j+1)

way = list(map(int, input().split()))
print(way)
res = "YES"
for i in range(1,len(way)):
    if parents[way[i-1]] != parents[way[i]]:
        res = "NO"

print(res)