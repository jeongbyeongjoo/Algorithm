import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = [input().strip() for _ in range(n)]
B = [input().strip() for _ in range(n)]

cnt = 0

for i in range(m-2):
    for j in range(i+1, m-1):
        for k in range(j+1, m):
            SET = {a[i] + a[j] + a[k] for a in A}

            flag = 0

            for b in B:
                if b[i] + b[j] + b[k] in SET:
                    flag = 1
                    break

            if not flag:
                cnt += 1

print(cnt)