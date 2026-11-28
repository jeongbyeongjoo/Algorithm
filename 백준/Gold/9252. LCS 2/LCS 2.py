A = input()
B = input()

prev = ['']*len(B)

if A[0] == B[0]:
    prev[0] = A[0]

for i in range(1, len(B)):
    if A[0] == B[i]:
        prev[i] = A[0]
    else:
        prev[i] = prev[i-1]

for i in range(1, len(A)):
    curr = ['']*len(B)

    if B[0] == A[i]:
        curr[0] = B[0]
    else:
        curr[0] = prev[0]

    for j in range(1, len(B)):
        if A[i] == B[j]:
            curr[j] = prev[j-1] + A[i]
        else:
            if len(prev[j]) > len(curr[j-1]):
                curr[j] = prev[j]
            else:
                curr[j] = curr[j-1]

    prev = curr

answer = prev[-1]

print(len(answer))
if answer:
    print(answer)