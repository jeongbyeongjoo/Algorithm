N = int(input())
price = [0] + list(map(int, input().split()))

INT_MIN = float('-inf')
dp = [INT_MIN for _ in range(N+1)]

dp[0] = 0

for i in range(1, N+1):
    for elem in range(1, N+1):
        if i >= elem:
            dp[i] = max(dp[i], dp[i-elem] + price[elem])

print(dp[N])