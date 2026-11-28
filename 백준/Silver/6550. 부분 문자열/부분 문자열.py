import sys

def solve():
    i = 0
    for j in range(m):
        while i < n and A[i] != B[j]:
            i += 1

        if i == n:
            return False

        if A[i] == B[j]:
            i += 1
            continue

    return True

for line in sys.stdin:
    B, A = line.split()
    n, m = len(A), len(B)

    if solve():
        print("Yes")
    else:
        print("No")