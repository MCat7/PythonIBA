class Table:
    # __length = None
    # __height = None
    # __weight = None
    # __mass = None

    def __init__(self, mass):
        self.mass = mass
        self.__length = 5
        self.__weight = 2
        self.__height = 1

    def get_mass(self):
        return self.mass

    def __str__(self):
        return (f'Стол {self.mass} кг')


class Truck:
    # __max_mass = None
    tables = []

    def __init__(self, max_mass):
        self.__max_mass = max_mass

    def get_max_mass(self):
        return self.__max_mass



print(f'Введите грузоподъёмность вашего грузовика: ')
max_mass = int(input())
myTruck = Truck(max_mass)
check = True

while check:
    current_mas_in_truck = 0
    print(f'Введите массу очередного стола: ')
    max_next_table = int(input())
    newTable = Table(max_next_table)
    print(newTable)
    myTruck.tables.append(newTable)
    for i in range(len(myTruck.tables)):
        current_mas_in_truck = current_mas_in_truck + myTruck.tables[i].get_mass()

    if current_mas_in_truck > myTruck.get_max_mass():
        print("В грузовик больше не влезет столов")
        myTruck.tables.pop(len(myTruck.tables) - 1)
        check = False

# for i in myTruck.tables:
#     print(i)
print(myTruck.tables)
