import sys
input = sys.stdin.readline

n = int(input())

points = []

for i in range(n):
    x1, x2, c = map(int, input().split())
    points.append((x1, 1, i, c))
    points.append((x2, -1, i, c))

points.sort(key=lambda x: (x[0], -x[1]))

active = set()
result = []

for x, v, index, c in points:
    if v == 1:
        if not active:
            start = x
            min_cost = c
        else:
            min_cost = min(min_cost, c)

        active.add(index)

    else:
        active.remove(index)

        if not active:
            result.append((start, x, min_cost))

print(len(result))

for s, e, c in result:
    print(s, e, c)