import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [input().rstrip('\n') for i in range(n)]

d = dict()
s = set()
ans = []

for elem in arr:
    if elem in s:
        d[elem] += 1
    else:
        d[elem] = 1
        s.add(elem)

for elem, cnt in d.items():
    ans.append((-cnt, -len(elem), elem))

ans.sort()

for elem in ans:
    cnt = -elem[0]
    length = -elem[1]
    word = elem[2]

    if length >= m:
        print(word)