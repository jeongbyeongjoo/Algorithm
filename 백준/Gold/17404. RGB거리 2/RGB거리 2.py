n = int(input())
grid = [[0]*3]

for _ in range(n):
    left, mid, right = map(int, input().split())
    grid.append([left, mid, right])

INT_MAX = float('inf')

dp1 = [[INT_MAX]*3 for _ in range(n+1)]
dp2 = [[INT_MAX]*3 for _ in range(n+1)]
dp3 = [[INT_MAX]*3 for _ in range(n+1)]

dp1[1][0] = grid[1][0]
dp1[1][1] = INT_MAX
dp1[1][2] = INT_MAX

dp2[1][0] = INT_MAX
dp2[1][1] = grid[1][1]
dp2[1][2] = INT_MAX

dp3[1][0] = INT_MAX
dp3[1][1] = INT_MAX
dp3[1][2] = grid[1][2]

for i in range(2, n+1):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp1[i][j] = min(dp1[i][j], dp1[i-1][k] + grid[i][j])

for i in range(2, n+1):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp2[i][j] = min(dp2[i][j], dp2[i-1][k] + grid[i][j])

for i in range(2, n+1):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp3[i][j] = min(dp3[i][j], dp3[i-1][k] + grid[i][j])

dp1[n][0] = INT_MAX
dp2[n][1] = INT_MAX
dp3[n][2] = INT_MAX

min1 = min(dp1[n])
min2 = min(dp2[n])
min3 = min(dp3[n])

print(min(min1, min2, min3))