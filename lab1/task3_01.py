# 1	Удалить элемент с введенным номером a.

import random
n = int(input('Укажите размер списка: '))
A = [random.randint(0, 99) for _ in range(n)]

print(f'A: {A}')
a = int(input('Укажите номер элемента для удаления: '))
print(f'Удалённый элемент: {A.pop(a-1)}')
print(f'A: {A}')