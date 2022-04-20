# 4	Найти значение минимального элемента списка.

import random

n = int(input('Укажите размер списка: '))
A = [random.randint(0, 99) for _ in range(n)]

print(f'A: {A}')
minimum = A[0]
for i in range(len(A)):
    if A[i] < minimum:
        minimum = A[i]
print(f'Минимум: {minimum}')
