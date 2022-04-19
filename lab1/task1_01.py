# 1	Ввести три числа m, n, p. Подсчитать количество отрицательных чисел.
import random
m, n, p = int(input("Введите число m: ")), \
          int(input("Введите число n: ")), \
          int(input("Введите число p: "))
l1 = list()
l1.append(m)
l1.append(n)
l1.append(p)
count = 0
for i in range(len(l1)):
    if l1[i] < 0:
        count += 1
print('l1: ' + str(l1))
print(f'Количество отрицательных чисел в l1: {count}')
count = 0
l2 = [random.randint(-10, 10) for _ in range(5)]
for i in range(len(l2)):
    if l2[i] < 0:
        count += 1
print('l2: ' + str(l2))
print(f'Количество отрицательных чисел в l2: {count}')
