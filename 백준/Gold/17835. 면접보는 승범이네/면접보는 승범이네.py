import sys
import heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
interview = list(map(int, input().split()))

INT_MAX = float('inf')

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
dist = [INT_MAX]*(n+1)
pq = []

for u, v, w in edges:
    graph[v].append((u, w))

for elem in interview:
    dist[elem] = 0
    heapq.heappush(pq, (0, elem))

while(pq):
    min_dist, u = heapq.heappop(pq)
    if not visited[u]:
        visited[u] = True
        for v, w in graph[u]:
            if min_dist + w < dist[v]:
                dist[v] = min_dist + w
                heapq.heappush(pq, (dist[v], v))

ans = max(dist[1:])

print(dist.index(ans, 1))
print(ans)