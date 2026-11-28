import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = [0] * (n+1)

INT_MIN = float('-inf')

for _ in range(n-1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dfs(u):
    for v, w in graph[u]:
        if not visited[v]:
            visited[v] = True
            cnt[v] = cnt[u] + w
            dfs(v)

visited[1] = True
dfs(1)

max_int = INT_MIN
data = 1

for i in range(1, n+1):
    if max_int < cnt[i]:
        max_int = cnt[i]
        data = i

for i in range(n+1):
    visited[i] = False
    cnt[i] = 0

visited[data] = True
dfs(data)

print(max(cnt))