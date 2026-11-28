import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
queries = [int(input()) for _ in range(m)]

arr.sort()

for elem in queries:
    right = len(arr) - 1
    left = 0
    ans = -1

    while left <= right:
        mid = (right + left) // 2

        if arr[mid] == elem:
            ans = mid
            right = mid - 1
        elif arr[mid] > elem:
            right = mid - 1
        elif arr[mid] < elem:
            left = mid + 1

    print(ans)