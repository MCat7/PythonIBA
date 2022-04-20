# 13 Найти для каждого элемента списка А сумму предыдущих
#       элементов и записать эти суммы в новый список B.

import random

n = int(input('Укажите размер списка: '))
A = [random.randint(0, 99) for _ in range(n)]
B = []
print(f'A: {A}')
for i in range(len(A)):
    sUm = 0
    for j in range(i):
        sUm += A[j]
    B.append(sUm)
print(f'B: {B}')
