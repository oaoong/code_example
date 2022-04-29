n, m = map(int, input().split())
li = [list(map(int, input())) for _ in range(n)]
count = 0

def dfs(graph, y, x, tag):
    global count
    try_count= False
    if(y-1>=0):
        if(graph[y-1][x]==0):
            graph[y-1][x]=1
            dfs(graph,y-1,x, False)
            try_count=True
    if(x-1>=0):
        if(graph[y][x-1]==0):
            graph[y][x-1]=1
            dfs(graph,y,x-1, False)
            try_count=True
    if(x+1<m):
        if(graph[y][x+1]==0):
            graph[y][x+1]=1
            dfs(graph,y,x+1, False)
            try_count=True
    if(y+1<n):
        if(graph[y+1][x]==0):
            graph[y+1][x]=1
            dfs(graph,y+1,x, False)
            try_count=True
    
    if(try_count & tag):
        count+=1
    
# visited = [[False for _ in range(m)]*n]
for i in range(n):
    for j in range(m):
        dfs(li, i, j, True)
        
print(count)
