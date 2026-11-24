s = input()

happy = 0
sad = 0

for elem in s:
    if elem in 'HAPPY':
        happy += 1
    if elem in 'SAD':
        sad += 1

if happy == 0 and sad == 0:
    print('50.00')
else:
    result = happy * 100000 // (happy + sad)
    result = (result + 5) // 10
    print(f'{result / 100:.2f}')