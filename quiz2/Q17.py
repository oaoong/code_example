import copy
N, K = map(int, input().split())
maps = []
temp = []
for i in range(N):
    maps.append(list(map(int, input().split())))
    temp.append(maps[i][:])
S, X, Y = map(int, input().split())

move_x = [0, 0, -1, 1]
move_y = [1, -1, 0, 0]

def virus(maps, x, y):
    now = maps[x][y]
    for i in range(4):
        new_x = x+move_x[i]
        new_y = y+move_y[i]
        if(new_x>=0 and new_x<N and new_y >= 0 and new_y<N):
            if(maps[new_x][new_y]==0):
                maps[new_x][new_y] = now

for k in range(S):
    for h in range(1, K+1):
        for i in range(N):
            for j in range(N):
                if(maps[i][j] == h and temp[i][j] == maps[i][j]):
                    virus(maps, i, j)
    temp = copy.deepcopy(maps)

print(maps[X-1][Y-1])
