n = int(input())
arr = list(map(int, input().split()))

INF = float('inf')
dp = [INF]*(n+1)
dp[0] = 0

for i in range(n):
    for j in range(i):
        if j + arr[j] >= i:
            if dp[j] != INF:
                dp[i] = min(dp[i], dp[j]+1)

if dp[n-1] == INF:
    print(-1)
else:
    print(dp[n-1])