import sys
input = sys.stdin.readline

n, q = map(int, input().split())

points1 = []
points2 = []

for i in range(n):
    l, r, y = map(int, input().split())
    points1.append(l)
    points2.append(r)

l = max(points1)
r = min(points2)

for i in range(q):
    p = int(input())
    print(max(0, l - p, p - r))