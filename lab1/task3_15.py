# 15	Удалить элементы, индексы которых кратны 3.

import random
n = int(input('Укажите размер списка: '))
A = [random.randint(0, 99) for _ in range(n)]

B = []
print(f'A: {A}')
for i in range(0, len(A)):
    if i % 3 != 0 or i == 0:
        B.append(A[i])
print(f'B: {B}')

