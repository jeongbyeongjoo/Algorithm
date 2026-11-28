import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())

edges = [tuple(map(int, input().split())) for _ in range(m)]

INT_MAX = float('inf')

graph = [[] for _ in range(n+1)]

for u, v, w in edges:
    graph[u].append((v,w))

pq = []
visited = [False]*(n+1)
dist = [INT_MAX]*(n+1)
dist[k] = 0

heapq.heappush(pq, (0, k))

while pq:
    min_dist, index = heapq.heappop(pq)

    if not visited[index]:
        visited[index] = True
        for v, w in graph[index]:
            if min_dist + w < dist[v]:
                dist[v] = min_dist + w
                heapq.heappush(pq, (dist[v], v))

for i in range(1, n+1):
    if dist[i] == INT_MAX:
        print("INF")
    else:
        print(dist[i])