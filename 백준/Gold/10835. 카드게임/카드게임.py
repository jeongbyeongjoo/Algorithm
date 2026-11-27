n = int(input())
first_cards = [0] + list(map(int, input().split()))
second_cards = [0] + list(map(int, input().split()))

INT_MIN = float('-inf')

dp = [[INT_MIN]*(n+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1, n+1):
    if first_cards[1] > second_cards[i]:
        dp[0][i] = dp[0][i-1] + second_cards[i]

for i in range(1, n+1):
    dp[i][0] = 0

for i in range(1, n+1):
    for j in range(1, n+1):

        # 양쪽 카드 버리기
        dp[i][j] = dp[i-1][j-1]

        # 왼쪽 카드만 버리기
        if j < n:
            dp[i][j] = max(dp[i][j], dp[i-1][j])

        # 오른쪽 카드만 버리고 점수 획득
        if i < n and first_cards[i+1] > second_cards[j]:
            dp[i][j] = max(dp[i][j], dp[i][j-1] + second_cards[j])

print(max([max(row) for row in dp]))