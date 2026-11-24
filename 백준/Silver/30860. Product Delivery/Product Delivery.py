import sys
input = sys.stdin.readline

n = int(input())

ans = 1
max_l = 0

for _ in range(n):
    l, m = map(int, input().split())

    if max_l > m:
        ans += 1
        max_l = l
    else:
        max_l = max(max_l, l)

print(ans)