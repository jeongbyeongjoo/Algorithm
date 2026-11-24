n, m = map(int, input().split())

A = []
B = []

for _ in range(n):
    row = list(map(int, input().split()))
    A.append(row)

for _ in range(n):
    row = list(map(int, input().split()))
    B.append(row)

arr = list(map(int, input().split()))

dist = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        dist[i][j] = abs(A[i][j]-B[i][j])

max_arr = [0]*n

for i in range(n):
    for j in range(n):
        max_arr[j] = max(dist[i][j], max_arr[j])

ans = 0
for elem in arr:
    ans += max_arr[elem-1]

print(ans)
