from bisect import *

li = [1, 2, 2, 3, 3, 4]
print(bisect_left(li, 2))  # 1
print(bisect_right(li, 2))  # 3
print(bisect_left(li, 4))  # 5
print(bisect_right(li, 4))  # 6
insort(li, 2)
print(li)  # [1, 2, 2, 2, 3, 3, 4]

res = bisect_right(li, 2) - bisect_left(li, 2)
print(res)  # 3