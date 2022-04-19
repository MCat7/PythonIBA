print("Введите 4 целых числа (через Enter): ")
A = int(input())
B = int(input())
C = int(input())
D = int(input())
arr = [A, B, C, D]
flag = False
for i in range(1, len(arr)):
    if arr[i] % 2 == 0:
        print("Есть минимум одно чётное")
        flag = True
        break
if not flag:
    print("Нет чётных ")
