# 4	По номеру месяца напечатать пору года.

def switch(n):
    switcher = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна',
                5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето',
                9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}
    return switcher.get(n, "Значение некорректно")
    # print(type(switcher))


num = int(input("Укажите номер месяца: "))
print(switch(num))


