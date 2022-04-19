# 12	Есть натуральное двузначное число n.
# Верно ли, что среди его цифр есть 1 или 9?
import random
n = random.randint(10, 99)
num = n
flag = False
while num != 0:
    x = num % 10
    if x == 1 or x == 9:
        flag = True
        break
    num = int(num // 10)
    # print(num)
print(n)
print(f'В числе есть 1 или 9:  {flag}')
