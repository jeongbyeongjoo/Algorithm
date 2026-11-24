n = int(input())
arr = list(map(int, input().split()))

left = 0
right = 0

for i in range(n):
    if left == right:
        left += arr[i]
    elif left > right:
        right += arr[i]
    elif left < right:
        left += arr[i]

diff = abs(left-right)

cnt = 0

cnt += diff // 100
diff = diff % 100

cnt += diff // 50
diff = diff % 50

cnt += diff // 20
diff = diff % 20

cnt += diff // 10
diff = diff % 10

cnt += diff // 5
diff = diff % 5

cnt += diff // 2
diff = diff % 2

cnt += diff // 1
diff = diff % 1

print(cnt)
