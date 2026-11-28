n = int(input())
arr = list(map(int, input().split()))
k = int(input())

dict = dict()

cnt = 0
for elem in arr:
    if k-elem in dict:
        cnt += dict[k-elem]

    if elem in dict:
        dict[elem] += 1
    else:
        dict[elem] = 1

print(cnt)