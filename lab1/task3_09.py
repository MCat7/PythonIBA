# 9 Найти среднее арифметическое элементов списка.

import random
n = int(input('Укажите размер списка: '))
A = [random.randint(0, 99) for _ in range(n)]

sum = 0
for i in range(1, len(A)):
    sum += A[i]
print(f'Среднее = {sum/len(A)}')