N, M = map(int, input().split())
coin = [int(input()) for _ in range(N)]

INT_MAX = float('inf')

dp = [INT_MAX]*(M+1)

dp[0] = 0
for i in range(M+1):
    for j in range(N):
        if i >= coin[j]:
            dp[i] = min(dp[i], dp[i-coin[j]] + 1)

if dp[M] == INT_MAX:
    print(-1)
else:
    print(dp[M])