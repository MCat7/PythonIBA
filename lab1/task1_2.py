# 2	Определить, имеется ли среди трёх чисел a, b и c хотя бы одна пара равных между собой чисел.
import random

flag = False
lis = [random.randint(0, 5) for _ in range(3)]
for i in range(0, len(lis) - 1):
    if not flag:
        for j in range(i + 1, len(lis)):
            # print(lis[i] == lis[j])
            if lis[i] == lis[j]:
                flag = True
                break
print('lis: ' + str(lis))
str1 = ""
if flag:
    str1 = "Есть"
else:
    str1 = "Нет"
print(f' Есть ли совпадения: {str1}')
