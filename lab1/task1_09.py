# import numpy as np
# for x in np.arange(0.0, 0.6, 0.1):
#     y = 2 ** x
#     print(y)


# 9 Проверить, является ли дробь A / B правильной.
print("Введите числитель: ")
A = int(input())
# print(A)
B = int(input("Введите знаменатель: "))
if abs(A) < abs(B):
    print("Дробь правильная")
else:
    print("Дробь неправильная")


