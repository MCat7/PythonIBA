# 2	Все четные по значению элементы исходного списка A поместить в новый список B.

import random
n = int(input('Укажите размер списка: '))
A = [random.randint(0, 99) for _ in range(n)]

B = []
print(f'A: {A}')
for i in range(len(A)):
    if A[i] % 2 == 0:
        B.append(A[i])
print(f'B: {B}')
