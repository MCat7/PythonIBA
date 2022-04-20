# 16 Найти номера минимального и максимального элементов первой половины списка.

import random

n = int(input('Укажите размер списка: '))
A = [random.randint(0, 99) for _ in range(n)]

print(f'A: {A}')
indexMin = 0
indexMax = 0
minEl = A[0]
maxEl = A[0]
for i in range(int(len(A)/2)):
    if A[i] < minEl:
        minEl = A[i]
        indexMin = i
    if A[i] > maxEl:
        maxEl = A[i]
        indexMax = i

print(f'Индекс минимального элемента первой половины списка: {indexMin}')
print(f'Индекс максимального элемента первой половины списка: {indexMax}')
