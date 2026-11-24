# 9분 45초
n = int(input())

arr = []

for _ in range(n):
    b, p, q, r = map(int, input().split())
    arr.append((p*q*r, p+q+r, b))

arr.sort()

for i in range(3):
    print(arr[i][2], end=" ")

