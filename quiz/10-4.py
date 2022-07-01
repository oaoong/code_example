from collections import deque

n = int(input())
indegree = [0] * (n+1)
times = [0] * (n+1)
graph = [[] for i in range(n+1)]

for i in range(1, n+1):
    inp = list(map(int, input().split()))
    times[i] = inp[0]
    for j in inp[1:-1]:
        graph[j].append(i)
        indegree[i] += 1

def topology_sort():
    print("times",times)
    result = times[:]
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                result[i] += result[now]
                q.append(i)

    print(*result[1:], sep="\n")



topology_sort()
