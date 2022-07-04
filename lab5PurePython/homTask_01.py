class TribonacciIterator:
    def __init__(self, n):
        self.n = n
        self.counter = 1


    def __iter__(self):
        return self

    def __next__(self):
        if self.counter in (3, 4) and self.counter <= self.n:
            self.counter += 1
            return 1
        elif self.counter in (1, 2) and self.counter <= self.n:
            self.counter += 1
            return 0
        elif self.counter <= self.n:
            x = (self.counter - 1) + (self.counter - 2) + (self.counter - 3)
            self.counter += 1
            return x
        else:
            raise StopIteration


if __name__ == '__main__':
    it = TribonacciIterator(20)
    for i in it:
        # вывод текущего элемента (который возвращает итератор)
        print(i)
