"""📌 Создайте класс окружность.
📌 Класс должен принимать радиус окружности при создании
экземпляра.
📌 У класса должно быть два метода, возвращающие длину окружности и её площадь."""
import math
import random


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def length_circle(self):
        return 2 * math.pi * self.radius

    def area_circle(self):
        return math.pi * pow(self.radius, 2)


"""📌 Создайте класс прямоугольник.
📌 Класс должен принимать длину и ширину при создании
экземпляра.
📌 У класса должно быть два метода, возвращающие периметр и площадь.
📌 Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат."""


class Rectangle:

    def __init__(self, length, width=None):
        self.length = length
        if width is None:
            self.width = length
        else:
            self.width = width

    def length_rectangle(self):
        return (self.length + self.width) * 2

    def area_rectangle(self):
        return self.length * self.width


"""📌 Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
📌 У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
📌 Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст."""


class Person:

    def __init__(self, name: str, last_name: str, family: str, age: int):
        self.name = name
        self.last_name = last_name
        self.family = family
        self.__age = age

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return f"Nane - {self.name}\nLast name - {self.last_name}\nFamily - {self.family = }\nAge - {self.__age}"


"""📌 Создайте класс Сотрудник.
📌 Воспользуйтесь классом человека из прошлого задания.
📌 У сотрудника должен быть:
    ○ шестизначный идентификационный номер
    ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь"""


class Employ(Person):

    def __init__(self, name: str, last_name: str, family: str, age: int, id_employ: int):
        super().__init__(name, last_name, family, age)
        if 0 > len(str(id_employ)) > 6:
            self.id_employ = random.randint(99999, 1000000)
        else:
            self.id_employ = id_employ
        self.access_level = sum([int(i) for i in str(id_employ)]) % 7


"""📌 Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
📌 У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
📌 Для каждого класса создайте метод, выводящий информацию специфичную для данного класса."""


class Animal:

    def __init__(self, name):
        self.name = name

    def all_info(self):
        print(f"name - {self.name}")


class Fish(Animal):

    def __init__(self, name, living_environment):
        super().__init__(name)
        self.living_environment = living_environment

    def all_info(self):
        super().all_info()
        print(f"living - {self.living_environment}")


class Bird(Animal):

    def __init__(self, name, type_birds):
        super().__init__(name)
        self.type_birds = type_birds

    def all_info(self):
        return f'type - {self.type_birds}'


class Dog(Animal):

    def __init__(self, name, living_environment):
        super().__init__(name)
        self.living_environment = living_environment

    def all_info(self):
        super().all_info()
        return f"living - {self.living_environment}"


"""📌 Доработайте задачу 5.
📌 Вынесите общие свойства и методы классов в класс
Животное.
📌 Остальные классы наследуйте от него.
📌 Убедитесь, что в созданные ранее классы внесены правки."""


