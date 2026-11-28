n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

sum_arr = [0] * (n + 1)

INT_MIN = float('-inf')

max = INT_MIN

for i in range(1, n+1):
    sum_arr[i] += sum_arr[i-1] + arr[i]

for i in range(k, n+1):
    data = sum_arr[i] - sum_arr[i-k]
    if data > max:
        max = data

print(max)
