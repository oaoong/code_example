import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for c in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])

x, k = map(int, input().split())
print(*graph)
print(graph[1][k] + graph[k][x]) if (graph[1][k] + graph[k][x] < INF) else print(-1)

