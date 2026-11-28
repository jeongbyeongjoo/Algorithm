n = int(input())
arr = list(map(int, input()))
target = list(map(int, input()))

def solve(arr, ans):
    for i in range(n-1):
        if arr[i] != target[i]:
            for j in range(0, 3):
                if i+j < n:
                    if arr[i+j] == 0:
                        arr[i+j] = 1
                    else:
                        arr[i+j] = 0
            ans += 1

    if arr[-1] != target[-1]:
        return float('inf')
    else:
        return ans

# 첫 번째 스위치를 누르지 않는 경우
ans1 = solve(arr[:], 0)

# 첫 번째 스위치를 누르는 경우
arr[0] = 1 - arr[0]
arr[1] = 1 - arr[1]

ans2 = solve(arr[:], 1)

answer = min(ans1, ans2)

if answer == float('inf'):
    print(-1)
else:
    print(answer)