import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dist = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(n):
        dist[i][j + 1] = row[j]

queries = [tuple(map(int, input().split())) for _ in range(m)]

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for x, y, t in queries:
    if dist[x][y] <= t:
        print("Enjoy other party")
    else:
        print("Stay here")