import sys
input = sys.stdin.readline

M, N = map(int, input().split())
temperature = [int(input()) for _ in range(M)]

clothes = [tuple(map(int, input().split())) for _ in range(N)]
s = [x[0] for x in clothes]
e = [x[1] for x in clothes]
v = [x[2] for x in clothes]

INT_MIN = float('-inf')
dp = [[INT_MIN]*N for _ in range(M)]

grid = [[INT_MIN]*N for _ in range(M)]

for i in range(M):
    for j in range(N):
        if s[j] <= temperature[i] <= e[j]:
            grid[i][j] = v[j]

for i in range(N):
    if grid[0][i] != INT_MIN:
        dp[0][i] = 0

for i in range(1, M):
    for j in range(N):
        if grid[i][j] == INT_MIN:
            continue

        for k in range(N):
            if dp[i-1][k] != INT_MIN:
                dp[i][j] = max(dp[i-1][k] + abs(grid[i][j]-grid[i-1][k]), dp[i][j])

print(max(dp[M-1]))