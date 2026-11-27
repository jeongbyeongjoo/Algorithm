import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

q = deque()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or a[x][y] == 1:
        return False
    return True

def bfs():
    while q:
        x, y = q.popleft()

        dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

        for dx, dy in zip(dxs, dys):
            new_x = dx + x
            new_y = dy + y
            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.append((new_x, new_y))

for j in range(m):
    if a[0][j] == 0:
        q.append((0, j))
        visited[0][j] = True

bfs()

if any(visited[n-1]):
    print("YES")
else:
    print("NO")