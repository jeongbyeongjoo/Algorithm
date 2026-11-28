from functools import cmp_to_key

n = int(input())
arr = list(map(int, input().split()))

def compare(x, y):
    x = str(x)
    y = str(y)
    if x+y > y+x:
        return -1
    if y+x > x+y:
        return 1
    return 0

arr.sort(key=cmp_to_key(compare))

if arr[0] == 0:
    print(0)
else:
    for elem in arr:
        print(elem, end="")