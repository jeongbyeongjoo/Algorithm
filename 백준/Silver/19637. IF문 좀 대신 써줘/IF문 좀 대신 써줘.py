import sys
from bisect import bisect_left
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
names = []

for _ in range(n):
    name, x = input().split()
    arr.append(int(x))
    names.append(name)

queries = [int(input()) for _ in range(m)]

for elem in queries:
    data = bisect_left(arr, elem)
    print(names[data])