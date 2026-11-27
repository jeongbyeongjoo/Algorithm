n = int(input())
m = int(input())

edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for elem in edges:
    graph[elem[0]].append(elem[1])
    graph[elem[1]].append(elem[0])

cnt = 0

def dfs(vertex):
    global cnt
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            cnt += 1
            visited[curr_v] = True
            dfs(curr_v)

visited[1] = True
dfs(1)
print(cnt)