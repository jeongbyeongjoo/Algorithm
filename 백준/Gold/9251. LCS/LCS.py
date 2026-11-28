A = input()
B = input()

dp = [[0]*len(B) for _ in range(len(A))]

if A[0] == B[0]:
    dp[0][0] = 1

for i in range(1, len(B)):
    if A[0] == B[i]:
        dp[0][i] = 1
    else:
        dp[0][i] = dp[0][i-1]

for i in range(1, len(A)):
    if B[0] == A[i]:
        dp[i][0] = 1
    else:
        dp[i][0] = dp[i-1][0]

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:   
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(A)-1][len(B)-1])
