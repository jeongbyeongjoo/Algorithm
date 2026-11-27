import sys
input = sys.stdin.readline

MOD = 1000000009

T = int(input())
arr = [int(input()) for _ in range(T)]
n = max(arr)

dp = [0]*(n+3)

dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD

for elem in arr:
    print(dp[elem])