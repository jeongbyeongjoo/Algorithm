A = '0' + input()
B = '0' + input()

grid = [[0]*len(B) for _ in range(len(A))]

if A[1] == B[1]:
    grid[1][1] = 0
else:
    grid[1][1] = 1

for i in range(2, len(B)):
    if A[1] == B[i]:
        grid[1][i] = i - 1
    else:
        grid[1][i] = grid[1][i-1] + 1

for i in range(2, len(A)):
    if B[1] == A[i]:
        grid[i][1] = i - 1
    else:
        grid[i][1] = grid[i-1][1] + 1

for i in range(2, len(A)):
    for j in range(2, len(B)):
        if A[i] == B[j]:
            grid[i][j] = grid[i-1][j-1]
        else:
            grid[i][j] = min(grid[i][j-1] + 1,
                             grid[i-1][j] + 1,
                             grid[i-1][j-1] + 1)

print(grid[-1][-1])