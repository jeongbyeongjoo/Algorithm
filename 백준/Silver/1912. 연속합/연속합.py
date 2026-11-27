n = int(input())
arr = list(map(int, input().split()))

INT_MIN = float('-inf')

dp = [INT_MIN]*(n+1)

dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + arr[i], arr[i])

print(max(dp))