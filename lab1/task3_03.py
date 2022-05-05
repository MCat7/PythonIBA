# 3	Удалить элементы, индексы которых кратны 7.

import random
n = int(input('Укажите размер списка: '))
A = [random.randint(0, 99) for _ in range(n)]

B = []
print(f'A: {A}')
for i in range(len(A)):
    if i % 7 != 0 or i == 0:
        B.append(A[i])
    else:
        B.append("")
print(f'B: {B}')
