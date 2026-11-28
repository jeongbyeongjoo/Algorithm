n, s = map(int, input().split())
arr = list(map(int, input().split()))

j = 0
sum = 0
min_val = float('inf')

for i in range(n):
    while j < n and sum < s:
        sum += arr[j]
        j += 1
    if sum >= s:
        min_val = min(min_val, j-i)
    sum -= arr[i]

if min_val == float('inf'):
    print(0)
else:
    print(min_val)