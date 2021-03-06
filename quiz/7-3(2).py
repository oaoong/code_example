# 이진 탐색을 이용한 파라메트릭 서치 문제 풀이
n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

#이진 탐색 수행(반복)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 덜 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 더 자르기(오른쪽 부분 탐색)
    else:
        result = mid # 최대한 더 잘랐을 때가 정답이므로 여기에서 result에 기록
        start = mid + 1
        
print(result)