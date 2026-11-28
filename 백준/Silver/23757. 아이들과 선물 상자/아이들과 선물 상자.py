import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))
children = list(map(int, input().split()))

heap = []

for elem in arr:
    heapq.heappush(heap, -elem)

for i in range(m):
    if -heap[0] < children[i]:
        print(0)
        break

    heapq.heappush(heap, heapq.heappop(heap)+children[i])

else:
    print(1)