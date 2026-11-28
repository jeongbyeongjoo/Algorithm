import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

edges = []

for _ in range(m):
    arr = list(map(int, input().split()))

    for i in range(1, len(arr)-1):
        edges.append((arr[i], arr[i+1]))

graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
cnt = 0

for u, v in edges:
    graph[u].append(v)
    indegree[v] += 1

q = deque()
result = []

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        cnt += 1

while q:
    u = q.popleft()
    result.append(u)

    for v in graph[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)
            cnt += 1

if cnt < len(graph) - 1:
    print(0)
else:
    for elem in result:
        print(elem)