# Задача на рекурсию
#
# Реализуйте рекурсивную функцию нарезания прямоугольника с заданными
# пользователем сторонами a и b на квадраты с наибольшей возможной
# на каждом этапе стороной. Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.
import prettytable

A = int(input("Введите длину стороны А: "))
B = int(input("Введите длину стороны В: "))

count = 0

table = prettytable.PrettyTable(["Итерация", "Сторона А", "Сторона B", "Количество квадратов"])


def delimeterRect(a, b):
    global count
    count += 1
    if a != 0 and b != 0:
        if a > b:
            x, y = a, b
        else:
            x, y = b, a
        table.add_row(["№ " + str(count), str(x), str(y), str(x // y)])
        delimeterRect(x % y, y)


delimeterRect(A, B)
print(table)
