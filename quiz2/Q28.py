from gettext import find


n = int(input())
li = list(map(int, input().split()))

def find_fixed_point(nums, start, end):
    while start <= end:
        mid = (start+end) // 2
        if nums[mid] == mid:
            return mid
        elif nums[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return -1

print(find_fixed_point(li, 0, len(li)))
