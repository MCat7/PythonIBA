# 8	Найти значение максимального элемента списка.

import random

n = int(input('Укажите размер списка: '))
A = [random.randint(0, 99) for _ in range(n)]

print(f'A: {A}')
maximum = A[0]
for i in range(len(A)):
    if A[i] > maximum:
        maximum = A[i]
print(f'Максимум: {maximum}')
