# 7. Составить алгоритм решения ребуса КОТ + КОТ = ТОК
# (различные буквы означают различные цифры, старшая буква ‒ не 0).

flag = False
for K in range(1, 10):
    for O in range(10):
        for T in range(1, 10):
            KOT = K * 100 + O * 10 + T
            TOK = T * 100 + O * 10 + K
            # print(KOT)
            # print(TOK)
            if KOT + KOT == TOK:
                print(f'{KOT} + {KOT} == {TOK}')
                flag = True
if not flag:
    print('Решения ребуса нет')