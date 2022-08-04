n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
cnt = []

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == j:
#             graph[i][j] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for k in range(1, n+1):
    res = 0
    for i in range(1, n+1):
        if graph[k][i] < INF:
            res += 1
        if graph[i][k] < INF:
            res += 1
    if res == n-1:
        cnt.append(k)

print(*graph, sep="\n")
print(cnt)