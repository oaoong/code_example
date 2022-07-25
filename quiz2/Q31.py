from collections import deque

T = int(input())


def get_largest_gold(y, x, gold_list):
    temp = [[0]*x for _ in range(y)]
    print(temp)
    for i in range(y):
        temp[i][0] = gold_list[i][0]
    print(temp)
    for i in range(1,x):
        for j in range(y):
            tt = []
            if (j-1>=0):
                tt.append(temp[j-1][i-1])
            tt.append(temp[j][i-1])
            if (j+1<y):
                tt.append(temp[j+1][i-1])
            temp[j][i] = max(tt) + gold_list[j][i]
    res = []
    for k in range(y):
        res.append(temp[k][x-1])
    print(temp)
    return max(res)


for _ in range(T):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    li = []
    for i in range(n):
        li.append([])
        for j in range(m):
            li[i].append(q.popleft())
    print(get_largest_gold(n, m, li))
