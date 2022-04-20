# 10	Найти среднее арифметическое трех последних элементов списка.
import random

n = int(input('Укажите размер списка: '))
A = [random.randint(0, 99) for _ in range(n)]

print(f'A: {A}')
sum = 0
for i in range(len(A) - 3, len(A)):
    sum += A[i]
avg = sum / 3
print('Среднее = ' + "%.3f" % avg)
