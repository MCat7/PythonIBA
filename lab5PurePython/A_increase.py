import time
# класс объектов-итераторов
# для указания текущего элемента
# в последовательности
class RangeIterator:
    # при создании создает переменные
    # для хранения текущего состояния
    def __init__(self, size):
        self.x = 0
        self.size = size

    # единственное, что можно делать с итератором -
    # двигать его на следующий элемент последовательности
    # это то, что делает итератор итератором
    def __next__(self):
        self.x += 1
        # если последовательность итератора
        # не бесконечна - должно быть условие
        # для окончания цикла
        if self.x > self.size:
            # для окончания цикла в итераторе
            # вызывается специальное исключение StopIteration
            raise StopIteration
        # возвращает элементы последовательности -
        # строки из решеток заданной длины
        return '#' * self.x


# класс итерируемых объектов
class RangeIterable:
    def __init__(self, size):
        self.size = size

    # для прохода по итерируемому объекту с помощью цикла
    # в начале цикла вызывается метод __iter__
    # для получения итератора
    # это то, что делает объект итерируемым
    def __iter__(self):
        return RangeIterator(self.size)

# главная программа с заголовком,
# позволяющим использовать этот файл как модуль:
if __name__ == '__main__':
    # создание итерируемого объекта
    main_iter = RangeIterable(32)
    # проход по итерируемому объекту с помощью цикла
    for line in main_iter:
        # вывод текущего элемента (который возвращает итератор)
        print(line)
        # задержка между выводами
        time.sleep(0.25)
