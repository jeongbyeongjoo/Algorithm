import sys
input = sys.stdin.readline

n = int(input())

points = []

for _ in range(n):
    x1, x2 = map(int, input().split())
    points.append((x1, +1))
    points.append((x2, -1))

points.sort()

sum = 0
ans = 0

for x, v in points:
    sum += v
    ans = max(ans, sum)

print(ans)