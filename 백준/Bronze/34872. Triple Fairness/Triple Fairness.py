n = int(input())

problem_cnt = [3]*n
cnt1 = [0]*n
cnt2 = [0]*n
cnt3 = [0]*n

for i in range(3*n):
    for j in range(n):
        if cnt1[j] == 0:
            cnt1[j] += 1
            print(j+1, end=" ")
        elif cnt2[j] == 0:
            cnt2[j] += 1
            print(j+1, end=" ")
        elif cnt3[j] == 0:
            cnt3[j] += 1
            print(j+1, end=" ")
