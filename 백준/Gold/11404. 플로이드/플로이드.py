import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

edges = [tuple(map(int, input().split())) for _ in range(m)]

INT_MAX = float('inf')
dist = [[INT_MAX]*(n+1) for _ in range(n+1)]

for u, v, w in edges:
    dist[u][v] = min(dist[u][v], w)

for i in range(1, n+1):
    dist[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == INT_MAX:
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()