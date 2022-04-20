# 12	Найти номер минимального элемента списка.

import random

n = int(input('Укажите размер списка: '))
A = [random.randint(0, 99) for _ in range(n)]

print(f'A: {A}')
minimum = A[0]
indexMinEl = 0
for i in range(len(A)):
    if A[i] < minimum:
        minimum = A[i]
        indexMinEl = i
print(f'Индекс минимального элемента: {indexMinEl}')
print(f'Позиция минимального элемента: {indexMinEl+1}')
