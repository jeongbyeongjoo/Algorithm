import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = [0] * (n+1)

def dfs(u):
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            cnt[v] = cnt[u] + 1
            dfs(v)

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited[1] = True
dfs(1)

max_int = 0
a = 1

for i in range(1, n+1):
    if max_int < cnt[i]:
        max_int = cnt[i]
        a = i

for i in range(n+1):
    visited[i] = False
    cnt[i] = 0

visited[a] = True
dfs(a)

print((max(cnt)+1)//2)