n, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = [0] * 100001

j = 0
INT_MIN = float('-inf')
ans = INT_MIN

for i in range(n):
    while j < n and cnt[arr[j]] < k:
        cnt[arr[j]] += 1
        j += 1
    cnt[arr[i]] -= 1
    ans = max(ans, j-i)

print(ans)