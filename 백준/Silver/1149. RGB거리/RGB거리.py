n = int(input())
grid = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n+1)]

for i in range(3):
    dp[1][i] = grid[1][i]

for i in range(2, n+1):
    for j in range(3):
        dp[i][j] = min(dp[i-1][j-1] + grid[i][j], dp[i-1][j-2] + grid[i][j])

print(min(dp[-1]))