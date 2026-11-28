import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    horizontal = [list(map(int, input().split())) for _ in range(n)]
    vertical = [list(map(int, input().split())) for _ in range(n - 1)]

    uf = [i for i in range(n*m)]
    size = [1] * (n*m)

    def union(x, y):
        X = find(x)
        Y = find(y)

        if X == Y:
            return False

        if size[X] > size[Y]:
            X, Y = Y, X

        uf[X] = Y
        size[Y] += size[X]
        return True

    def find(x):
        if uf[x] == x:
            return x
        uf[x] = find(uf[x])
        return uf[x]

    edges = []

    for i in range(n):
        for j in range(m-1):
            edges.append((m*i+j, m*i+j+1, horizontal[i][j]))

    for i in range(n-1):
        for j in range(m):
            edges.append((m*i+j, m*(i+1)+j, vertical[i][j]))

    edges.sort(key=lambda x:x[2])

    ans = 0
    cnt = 0

    for u, v, w in edges:
        if union(u, v):
            ans += w
            cnt += 1

            if cnt == n*m-1:
                break

    print(ans)

t = int(input())

for _ in range(t):
    solve()