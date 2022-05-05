from collections import deque
locx = 0
locy = 0
n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

def find_min_time(startx, starty, map_loc):
    queue = deque([[starty, startx, 2]])
    
    while queue:
        v = queue.popleft()
        print(*map_loc, sep='\n')
        print('---------------')
        
        map_loc[v[0]][v[1]] = v[2]
        if(v[1]+1<m):
            if(map_loc[v[0]][v[1]+1]==1): queue.append([v[0], v[1]+1, v[2]+1])
        if(v[1]-1>=0):
            if(map_loc[v[0]][v[1]-1] == 1 ): queue.append([v[0], v[1]-1, v[2]+1])
        if(v[0]+1<n):
            if(map_loc[v[0]+1][v[1]] == 1 ): queue.append([v[0]+1, v[1], v[2]+1])
        if(v[0]-1>=0):
            if(map_loc[v[0]-1][v[1]] == 1): queue.append([v[0]-1, v[1], v[2]+1])    
            
    return(map_loc[n-1][m-1]-1)
    
print(find_min_time(0, 0, maze))
