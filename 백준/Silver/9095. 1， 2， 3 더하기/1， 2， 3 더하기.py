import sys
input = sys.stdin.readline

def choose(current_number):
    global count

    # 종료조건
    if current_number == n:
        count += 1
        return
    elif current_number >= n:
        return

    # 재귀호출
    for i in range(1, 4):
        choose(current_number+i)

T = int(input())

for _ in range(T):
    n = int(input())
    count = 0

    choose(0)
    print(count)