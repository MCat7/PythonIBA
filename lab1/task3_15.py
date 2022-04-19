# 15	Удалить элементы, индексы которых кратны 3.

import random

arr = [random.randint(0, 200) for _ in range(10)]
arr1 = []
print(arr)
for i in range(0, len(arr)):
    if i % 3 != 0 or i == 0:
        arr1.append(arr[i])
print(arr1)

