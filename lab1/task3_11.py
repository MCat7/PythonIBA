# 11 Удалить пять первых нечетных по значению элементов списка.
import random

n = int(input('Укажите размер списка: '))
A = [random.randint(0, 99) for _ in range(n)]

print(f'A: {A}')
count = 0
deleted_elements = dict()
for i in range(len(A)):
    if A[i] % 2 != 0:
        deleted_elements.__setitem__(i, A[i])
        count += 1
        A[i] = "del"
        if count == 5:
            break
for i in range(len(A) - 1, -1, -1):
    if A[i] == 'del':
        A.pop(i)
print(f'Удаленные элементы (индекс: элемент): \n{deleted_elements}')
print(f'A: {A}')
