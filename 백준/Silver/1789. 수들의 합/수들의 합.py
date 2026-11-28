s = int(input())

left = 0
right = 10000000000
mid_num = -1

while left <= right:
    mid = (left + right) // 2
    if mid * (mid + 1) / 2 <= s:
        left = mid + 1
        mid_num = max(mid_num, left)
    else:
        right = mid - 1

print(mid_num-1)
