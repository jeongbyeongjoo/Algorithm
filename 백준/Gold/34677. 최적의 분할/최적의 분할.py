n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
cnt = 0
idx = 0
a_ar = [0] * n
b_ar = [0] * n

while(idx < n):
    a_min = idx
    b_min = idx
    for i in range(idx,n):
        if a[a_min] > a[i]:
            a_min = i
        if b[b_min] > b[i]:
            b_min = i
        a_ar[i] = a_min
        b_ar[i] = b_min
    for i in range(n-1,idx-1,-1):
        if idx == i:
            cnt += 1
            idx += 1
            break
        if a_ar[i] == b_ar[i]:
            cnt += 1
            idx = i +1
            break
print(cnt)
