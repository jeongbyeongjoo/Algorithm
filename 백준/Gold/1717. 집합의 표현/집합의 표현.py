import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(m)]

uf = [i for i in range(n+1)]

def union(x, y):
    uf[find(x)] = find(y)

def find(x):
    if uf[x] == x:
        return x
    root = find(uf[x])
    uf[x] = root
    return root

for act, x, y in query:
    if act == 0:
        union(x, y)
    else:
        if find(x) == find(y):
            print("YES")
        else:
            print("NO")