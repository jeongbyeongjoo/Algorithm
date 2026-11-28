import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(n-1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dfs(u, target, weight):
    if u == target:
        print(weight)
        return

    for v, w in graph[u]:
        if not visited[v]:
            visited[v] = True
            dfs(v, target, weight + w)

for _ in range(m):
    u, v = map(int, input().split())

    visited = [False] * (n+1)
    visited[u] = True

    dfs(u, v, 0)