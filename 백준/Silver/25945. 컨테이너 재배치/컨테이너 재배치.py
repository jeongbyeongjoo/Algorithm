n = int(input())
heights = tuple(map(int, input().split()))
m = sum(heights)

cnt = 0
higher = 0

for h in heights:
    if h > m // n:
        cnt += h - m // n
        higher += 1

cnt -= min(higher, m % n)

print(cnt)