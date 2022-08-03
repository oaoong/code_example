n = int(input())
pyramid = []
res = []
for _ in range(n):
    pyramid.append(list(map(int, input().split())))

for i in range(n):
    res.append([0]*len(pyramid[i]))

def find_max(pyramid, depth, loc, before):
    res[depth][loc] = max(res[depth][loc], pyramid[depth][loc] + before)
    if depth+1 >= n:
        return 0
    find_max(pyramid, depth+1, loc, res[depth][loc])
    find_max(pyramid, depth+1, loc+1, res[depth][loc])

find_max(pyramid, 0, 0, 0)
print(res)
print(max(res[n-1]))