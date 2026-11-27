k = int(input())

s = bin(k + 1)[3:]

ans = ""

for elem in s:
    if elem == "0":
        ans += "4"
    else:
        ans += "7"

print(ans)