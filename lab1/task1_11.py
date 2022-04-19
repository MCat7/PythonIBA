# 11	Даны три числа a, b, c. Значение наибольшего из них присвоить переменной d.
import random

arr = [random.randint(0, 100) for _ in range(3)]
# a = arr[0]
# b = arr[1]
# c = arr[2]
print(arr)
d = arr[0]
for i in range(1, len(arr)):
    if arr[i] > d:
        d = arr[i]
print('Максимальное число: ' + str(d))
