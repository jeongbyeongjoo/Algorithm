# 못품

N, M = map(int, input().split())
arr = []

def print_arr():
    for elem in arr:
        print(elem, end=' ')
    print()

def choose(num, cnt):
    if num == N+1:
        if cnt == M:
            print_arr()
        return

    arr.append(num)
    choose(num+1, cnt + 1)
    arr.pop()

    choose(num+1, cnt)


choose(1, 0)
