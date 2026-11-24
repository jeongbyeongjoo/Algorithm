# 9분 43초

n = int(input())

d = dict()

for _ in range(n):
    i, j, k = input().split()
    i = int(i)
    k = int(k)
    d[i] = (j, k)

x = int(input())

for i in range(n):
    j, k = d[x]
    if j == 'L':
        x = x - k
    elif j == 'R':
        x = x + k

print(x)
