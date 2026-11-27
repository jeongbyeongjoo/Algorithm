import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = []

def print_arr():
    print(' '.join(map(str, arr)))

def choose(num):
    if num == N:
        print_arr()
        return

    for i in range(K):
        arr.append(i+1)
        choose(num+1)
        arr.pop()

choose(0)