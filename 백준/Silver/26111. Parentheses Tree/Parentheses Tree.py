# 22분 30초

s = input()

stack = []
ans = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
    elif s[i] == ')':
        stack.pop()
        if i > 1 and s[i-1] == '(':
            ans += len(stack)

print(ans)
