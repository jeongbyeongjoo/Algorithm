# 12분

n = int(input())
visited = [False]*(n+1)
arr = []

def print_arr():
    for elem in arr:
        print(elem, end=' ')
    print()

def choose(num):
    if num == n:
        print_arr()
        return

    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        arr.append(i)
        choose(num+1)
        arr.pop()
        visited[i] = False

choose(0)

