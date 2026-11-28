import sys
import heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    pq = []

    for elem in arr:
        heapq.heappush(pq, elem)

    sum = 0
    cnt = 0

    while len(pq) > 1:
        data1 = heapq.heappop(pq)
        data2 = heapq.heappop(pq)
        sum = data1 + data2
        cnt += sum
        heapq.heappush(pq, sum)

    print(cnt)