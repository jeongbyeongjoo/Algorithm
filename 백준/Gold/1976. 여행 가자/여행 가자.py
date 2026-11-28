n = int(input())
k = int(input())

edges = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            edges.append((i+1, j+1))

path = list(map(int, input().split()))

uf = [i for i in range(n+1)]

def union(x, y):
    uf[find(x)] = find(y)

def find(x):
    if uf[x] == x:
        return x
    root_node = find(uf[x])
    uf[x] = root_node
    return root_node

for x, y in edges:
    union(x, y)

ans = 1

for i in range(1, k):
    if find(path[i-1]) != find(path[i]):
        ans = 0
        break

if ans == 1:
    print("YES")
else:
    print("NO")