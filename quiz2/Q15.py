from collections import deque
n, m, k, x = map(int, input().split())
city = [[] for _ in range(n+1)]
times = [0]*(n+1)
visited = [False] * (n+1)
result = []
for _ in range(m):
    a, b = map(int, input().split())
    city[a].append(b)

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    time = 0
    while q:
        v = q.popleft()
        time += 1
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                times[i] = time
                visited[i] = True
    print(graph)

bfs(city, x, visited)
for i in range(n+1):
    if times[i] == k:
        result.append(i)
print(times)
if len(result) == 0:
    print(-1)
else:
    for i in range(len(result)):
        print(result[i])