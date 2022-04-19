# Найти среднее арифметическое элементов списка.

import random

arr = [random.randint(0, 200) for _ in range(10)]
sum = 0
for i in range(1, len(arr)):
    sum += arr[i]
print(f'Среднее = {sum/len(arr)}')