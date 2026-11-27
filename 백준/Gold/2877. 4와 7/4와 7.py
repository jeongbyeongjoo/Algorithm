import sys
input = sys.stdin.readline

k = int(input())

arr = []

while True:
    if k == 1:
        arr.append('4')
        break
    elif k == 2:
        arr.append('7')
        break

    if k % 2 == 1:
        arr.append('4')
    else:
        arr.append('7')

    k = (k - 1) // 2

for elem in arr[::-1]:
    print(elem, end="")