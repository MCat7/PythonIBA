# 8	Дано натуральное четырехзначное число n. Верно ли, что все его цифры различны?
import random

n = random.randint(1000, 9999)
num = n
all_numbers_is_diff = True
A = list()
while num != 0:
    A.append(num % 10)
    num //= 10

for i in range(0, len(A) - 1):
    for j in range(i + 1, len(A)):
        if A[i] == A[j]:
            all_numbers_is_diff = False
            break
# print(A)
print(f'Все цифры числа {n} различны:  {all_numbers_is_diff}')
