n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

L = [0]*n

L[0] = cost[0]
for i in range(1, n):
    L[i] = min(L[i-1], cost[i])

sum = 0
for i in range(len(dist)):
    sum += L[i]*dist[i]

print(sum)
