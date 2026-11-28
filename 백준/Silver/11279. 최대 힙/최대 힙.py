import sys
import heapq
input = sys.stdin.readline

N = int(input())
commands = [int(input()) for _ in range(N)]

heap = []

for elem in commands:
    if elem != 0:
        heapq.heappush(heap, -elem)
    else:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)