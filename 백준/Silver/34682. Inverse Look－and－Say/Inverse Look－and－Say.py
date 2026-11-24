n = input()
x = ''

visited = [False]*11

flag = False

if len(n) % 2 == 0:
    for i in range(len(n)):
        if i % 2 == 1:
            if visited[int(n[i])]:
                flag = True
            visited[int(n[i])] = True
            if i > 1:
                visited[int(n[i-2])] = False
            else:
                if n[1] == '0':
                    flag = True
        else:
            for j in range(int(n[i])):
                x += n[i+1]
            if n[i] == '0':
                flag = True
else:
    flag = True

if not flag:
    print(x)
else:
    print(-1)

