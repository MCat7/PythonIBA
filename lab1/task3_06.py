# 6	Удалить все элементы с заданным значением, если они имеются в списке.
import random

n = int(input('Укажите размер списка: '))
A = [random.randint(0, 10) for _ in range(n)]

print(f'A: {A}')
delNum = int(input("Какое число удалить? "))
for i in range(len(A)-1, -1, -1):
    if A[i] == delNum:
        A.pop(i)
print(f'A: {A}')