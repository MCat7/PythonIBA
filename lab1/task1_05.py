# 5	Определить, есть ли среди заданных целых чисел A, B, C, D хотя бы одно нечётное.
import random

print("Сгенерировано 4 целых числа: ")
A = random.randint(-10, 10)
B = random.randint(-10, 10)
C = random.randint(-10, 10)
D = random.randint(-10, 10)
arr = [A, B, C, D]
print(arr)
flag = False
for i in range(0, len(arr)):
    if arr[i] % 2 != 0:
        print("Есть минимум одно нечётное")
        flag = True
        break
if not flag:
    print("Нет нечётных ")
