import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
parent = [0] * (n+1)

for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(u):
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            dfs(v)

visited[1] = True

dfs(1)

for i in range(2, n+1):
    print(parent[i])