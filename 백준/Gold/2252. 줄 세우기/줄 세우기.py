# 7분 52초
# sys 넣어야됨....

import sys

sys.setrecursionlimit(100000)

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for u, v in edges:
    graph[u].append(v)

stack = []

def dfs(x):
    for v in graph[x]:
        if not visited[v]:
            visited[v] = True
            dfs(v)

    stack.append(x)

for i in range(1, n+1):
    if not visited[i]:
        visited[i] = True
        dfs(i)

for elem in stack[::-1]:
    print(elem, end=" ")
