import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())

graph = [[] for _ in range(n+1)]
dp = [0] * (n+1)
arr = [0] * (n+1)

for i in range(2, n+1):
    t, a, p = input().split()
    a, p = int(a), int(p)

    if t == 'S':
        arr[i] = a
    else:
        arr[i] = -a

    graph[p].append(i)

def dfs(u):
    for v in graph[u]:
        dfs(v)

    dp[u] = arr[u]

    for v in graph[u]:
        if dp[v] > 0:
            dp[u] += dp[v]

dfs(1)

print(dp[1])