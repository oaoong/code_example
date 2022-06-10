# 이진 탐색을 이용한 풀이
n = int(input())
li = sorted(list(map(int, input().split())))
print(li)
m = int(input())
target = list(map(int, input().split()))

def binary_search(target, array, start, end):
    mid = (start + end) // 2
    if(start>end):
        return 
    if(target == array[mid]):
        return True
    elif(target > array[mid]):
        return binary_search(target, array, mid+1, end)
    else:
        return binary_search(target, array, start, mid-1)
    
for el in target:
    if(binary_search(el, li, 0, n-1)) == True:
        print("yes", end=" ")
    else:
        print("no", end=" ")
        

# 시간 복잡도
# 정렬 과정 O(N x log(N)) + 탐색 과정 O(M x log(N)) = O((M+N) x log(N))