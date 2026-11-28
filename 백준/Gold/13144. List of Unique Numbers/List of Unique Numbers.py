n = int(input())
arr = list(map(int, input().split()))
cnt = [0] * 100001

j = 0
ans = 0

for i in range(n):
    while j < n and cnt[arr[j]] < 1:
        cnt[arr[j]] += 1
        j += 1
    cnt[arr[i]] -= 1
    ans += j-i

print(ans)