n, m = map(int, input().split())
parent = [0] * (n+1)

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def check_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        print("NO")
    else:
        print("YES")

for i in range(n+1):
    parent[i] = i

for i in range(m):
    k, a, b = map(int, input().split())
    if k==0:
        union_parent(parent, a, b)
    else:
        check_parent(parent, a, b)
