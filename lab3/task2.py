import datetime


def tribonacci(n):
    if n in (1, 2):
        return 0
    elif n == 3:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


n = 20
t1 = datetime.datetime.now()
print(tribonacci(n))
t2 = datetime.datetime.now()
print(str((t2 - t1).total_seconds()))
