# 14 Найти индексы первого и последнего нулевых элементов списка.

import random

n = int(input('Укажите размер списка: '))
A = [random.randint(0, 5) for _ in range(n)]

# 1-ый вариант
print(f'A: {A}')
indexFirstZero = -1
indexLastZero = -1
for i in range(len(A)):
    if A[i] == 0:
        indexFirstZero = i
        break
for i in range(len(A) - 1, 0, -1):
    if A[i] == 0:
        indexLastZero = i
        break
if indexFirstZero == -1:
    print("Нет нулевых элементов")
else:
    print(f'Индекс первого нулевого элемента: {indexFirstZero}')
    print(f'Индекс последненго нулевого элемента: {indexLastZero}')

# 2-ой вариант
try:
    print(f'Индекс первого нулевого элемента: {A.index(0)}')
    A.reverse()
    print(f'Индекс последненго нулевого элемента: {len(A) - 1 - A.index(0)}')

except Exception:
    print("В списке нет нулей")