n, b, a = map(int, input().split())

arr = [0] + list(map(int, input().split()))

arr.sort()

sum_arr = [0]*(n+1)
max_int = 0
ans = 0

for i in range(1, n+1):
    sum_arr[i] = sum_arr[i-1] + arr[i]

for i in range(1, n+1):
    if i < a:
        data = sum_arr[i]/2
        if max_int < data and b >= data:
            ans = i
    elif i >= a:
        data = sum_arr[i-a] + (sum_arr[i] - sum_arr[i-a])/2
        if max_int < data and b >= data:
            ans = i

print(ans)
