# 16	По введенному числу (от 0 до 7) напечатать название цифры.

def switch(n):
    switcher = {0: 'Ноль', 1: 'Один', 2: 'Два', 3: 'Три',
                4: 'Четыре', 5: 'Пять', 6: 'Шесть', 7: 'Семь'}
    return switcher.get(n, "Значение некорректно")
    # print(type(switcher))


num = int(input("Укажите число от 0 до 7: "))
print('Вы ввели: ' + switch(num))
