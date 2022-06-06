# Вариант 2
# Введите одномерный целочисленный список. Найдите наибольший нечетный элемент.
# Найдите минимальный по модулю элемент списка.

import random as r

A = [r.randint(-50, 20) for _ in range(30)]
print(A)
A.sort()
A.reverse()
max_even_number = -1
# print(A)
for i in A:
    if i % 2 != 0:
        max_even_number = i
        break
print(f"наибольший нечетный элемент: {max_even_number}")
min_ABS_number = A[0]
for i in range(len(A)):
    if abs(A[i]) < abs(min_ABS_number):
        min_ABS_number = A[i]
# print(A)
print(f"минимальный по модулю элемент списка: {min_ABS_number}")
