# Kласс Airline:
# Пункт назначения,
# Номер рейса,
# Тип самолета,
# Время вылета,
# Дни недели.
# Функции- члены реализуют запись и считывание полей (проверка корректности).
# Создать список объектов. Вывести:
# a) список рейсов для заданного пункта назначения;
# б) список рейсов для заданного дня недели;.

class Airline:
    _aircraft_type = "BOEING"

    def __init__(self, destination, flight_number,
                 departure_time, days_of_the_week):
        self.__destination = destination
        self.__flight_number = flight_number
        self.__departure_time = departure_time
        self.__days_of_the_week = days_of_the_week

    def get_destination(self):
        return self.__destination

    def set_destination(self, destination):
        self.__destination = destination
        return

    def get_flight_number(self):
        return self.__flight_number

    def set_flight_number(self, flight_number):
        self.__flight_number = flight_number
        return

    def get_aircraft_type(self):
        return self.__aircraft_type

    def set_aircraft_type(self, aircraft_type):
        self.__aircraft_type = aircraft_type
        return

    def get_departure_time(self):
        return self.__departure_time

    def set_departure_time(self, departure_time):
        self.__departure_time = departure_time
        return

    def get_days_of_the_week(self):
        return self.__days_of_the_week

    def set_days_of_the_week(self, days_of_the_week):
        self.__days_of_the_week = days_of_the_week
        return

    def __str__(self):
        str_days = ""
        for i in self.get_days_of_the_week():
            if self.get_days_of_the_week()[i]:
                str_days = str_days + "," + i
        return f"Пункт назначения: {self.__destination}\n" \
               f"Номер рейса: {self.__flight_number}\n" \
               f"Тип самолета: {self._aircraft_type}\n" \
               f"Время вылета: {self.__departure_time}\n" \
               f"Дни недели: {str_days} "


def days():
    days = {"Пн": False, "Вт": False, "Ср": False, "Чт": False, "Пт": False, "Сб": False, "Вс": False}
    print("В какие дни недели состоятся вылеты? Ввводите \"Y\" или \"N\"")
    for i in days:
        # print(f"День недели {i}:")
        if str(input(f"День недели {i}:")).upper() == "Y":
            days[i] = True
        else:
            days[i] = False
    return days


air = Airline("Vilnus", 1123, "12.00", days())

print(air)