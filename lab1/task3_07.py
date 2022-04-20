# 7	Удалить из списка все элементы, совпадающие с его минимальным значением.
import random

n = int(input('Укажите размер списка: '))
A = [random.randint(0, 10) for _ in range(n)]

print(f'A: {A}')
minimum = A[0]
for i in range(len(A)):
    if A[i] < minimum:
        minimum = A[i]
for i in range(len(A)-1, -1, -1):
    if A[i] == minimum:
        A.pop(i)
print(f'A: {A}')
print(f'minimum: {minimum}')