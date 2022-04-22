# 3. О каждом учащемся класса известны его пол, год рождения, рост и вес.
# Определить, сколько в классе мальчиков и сколько девочек.
# Найти средний возраст мальчиков и девочек.
# Определить, верно ли, что самый высокий мальчик весит больше всех в классе,
# а самая маленькая девочка является самой юной среди девочек.
import datetime
import random
import math

current_date = datetime.datetime.now()


class Student:
    def __init__(self, id, gender, year_of_birth, height, weight):
        self.id = id
        self.gender = gender
        self.year_of_birth = year_of_birth
        self.height = height
        self.weight = weight

    def __str__(self):
        return f'id= {self.id} ' \
               f"Пол: {self.gender}  " \
               f"Год рождения: {self.year_of_birth} " \
               "Рост: " + "%.2f" % self.height + " " \
                                                 f"Вес: {self.weight} "

    def get_w(self):
        return int(self.weight)

    def get_h(self):
        return int(self.height * 100)

    def get_year(self):
        return int(self.year_of_birth)


def sort_weight(student):
    return student.get_w()


def sort_height_boys(student):
    if student.gender == 'мужской':
        return student.get_h()
    else:
        return 0


def sort_young_girls(student):
    if student.gender == 'женский':
        return student.get_year()
    else:
        return 0


def sort_height_girls(student):
    if student.gender == 'женский':
        return student.get_h()
    else:
        return 10000


def random_gender():
    genders = {1: 'мужской', 2: 'женский'}
    i = random.randint(1, 2)
    return genders.get(i)


def random_year():
    return random.randint(2005, 2007)


def random_height():
    return random.randint(150, 180) / 100


def random_weight():
    return random.randint(50, 80)


def new_student(id):
    return Student(id, random_gender(), random_year(), random_height(), random_weight())


list_of_students = []
for i in range(10):
    list_of_students.append(new_student(i + 1))

for i in range(len(list_of_students)):
    print(list_of_students[i])

boys = 0
girls = 0
sum_boys_age = 0
sum_girls_age = 0
for i in range(len(list_of_students)):
    if list_of_students[i].gender == 'мужской':
        boys += 1
        sum_boys_age += current_date.year - list_of_students[i].year_of_birth
    else:
        girls += 1
        sum_girls_age += current_date.year - list_of_students[i].year_of_birth

print(f'Boys: {boys}')
print(f'Girls: {girls}')
print(f'Средний возраст мальчиков: {math.ceil(sum_boys_age / boys)}')
print(f'Средний возраст девочек: {math.ceil(sum_girls_age / girls)}')

max_height_boy = max(list_of_students, key=sort_height_boys)
max_weight_stud = max(list_of_students, key=sort_weight)
print(f'Самый тяжелый ученик: {max_weight_stud}')
print(f'Самый высокий мальчик: {max_height_boy}')

check = False
if max_height_boy.id != max_weight_stud.id:
    check = False
else:
    check = True
print(f'Самый высокий мальчик весит больше всех в классе: {check}')

min_age_girl = max(list_of_students, key=sort_young_girls)  # max, так как год рождения
min_height_girl = min(list_of_students, key=sort_height_girls)

check = False
if min_age_girl.id != min_height_girl.id:
    check = False
else:
    check = True
print("")
print(f'Самая юная девочка: {min_age_girl}')
print(f'Самая маленькая девочка: {min_height_girl}')
print(f'Самая маленькая девочка является самой юной среди девочек: {check}')
