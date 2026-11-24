A, B, C, D, E, F, G, H = map(int, input().split())

cnt = 0

visited = [False]*14

for d in range(1, 14):
    if not visited[d]:
        for h in range(1, 14):
            if not visited[h]:
                if D != d + h:
                    continue
                if d == h:
                    continue
                visited[d] = True
                visited[h] = True
                for l in range(1, 14):
                    if not visited[l]:
                        for m in range(1, 14):
                            if not visited[m]:
                                if H != l + m:
                                    continue
                                if m == l:
                                    continue
                                visited[m] = True
                                visited[l] = True
                                for c in range(1, 14):
                                    if not visited[c]:
                                        for g in range(1, 14):
                                            if not visited[g]:
                                                for k in range(1, 14):
                                                    if not visited[k]:
                                                        if C != c + g + k:
                                                            continue
                                                        if c == g or g == k or k == c:
                                                            continue
                                                        visited[c] = True
                                                        visited[g] = True
                                                        visited[k] = True
                                                        for i in range(1, 14):
                                                            if not visited[i]:
                                                                for j in range(1, 14):
                                                                    if not visited[j]:
                                                                        if G != i + j + k:
                                                                            continue
                                                                        if i == j or j == k or k == i:
                                                                            continue
                                                                        visited[i] = True
                                                                        visited[j] = True
                                                                        for b in range(1, 14):
                                                                            if not visited[b]:
                                                                                for f in range(1, 14):
                                                                                    if not visited[f]:
                                                                                        if B != b + f + j + m:
                                                                                            continue
                                                                                        if b == f:
                                                                                            continue
                                                                                        visited[b] = True
                                                                                        visited[f] = True
                                                                                        for e in range(1, 14):
                                                                                            if not visited[e]:
                                                                                                if F != e + f + g + h:
                                                                                                    continue
                                                                                                visited[e] = True
                                                                                                for a in range(1, 14):
                                                                                                    if A != a + e + i + l:
                                                                                                        continue
                                                                                                    if E != a + b + c + d:
                                                                                                        continue
                                                                                                    cnt += 1
                                                                                                visited[e] = False
                                                                                        visited[b] = False
                                                                                        visited[f] = False
                                                                        visited[i] = False
                                                                        visited[j] = False
                                                        visited[c] = False
                                                        visited[g] = False
                                                        visited[k] = False
                                visited[m] = False
                                visited[l] = False
                visited[d] = False
                visited[h] = False

print(cnt)
