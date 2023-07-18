"""📌 Создайте класс Моя Строка, где:
📌 будут доступны все возможности str
📌 дополнительно хранятся имя автора строки и время создания (time.time)"""
import time


class MyString(str):
    """"A class that contains the instance creation time"""

    def __init__(self, text):
        self.text = text
        self.time_create = time.time()


test = MyString("Hello")

# print(test + ' World!', test.time_create)


"""
📌 Создайте класс Архив, который хранит пару свойств. Например, число и строку.
📌 При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков- архивов
📌 list-архивы также являются свойствами экземпляра"""


class Archive:
    """Class for creating an archive of instances"""

    list_archive_name: list = []
    list_archive_age: list = []

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.name_archive = self.list_archive_name.copy()
        self.age_archive = self.list_archive_age.copy()
        self.list_archive_age.append(age)
        self.list_archive_name.append(name)

    def __str__(self):
        return f"name = {self.name}\nage = {self.age}\nArchive = {self.name_archive}|{self.age_archive}"

    def __repr__(self):
        return f"Archive('{self.name}', {self.age})"


test1 = Archive('test1', 1)
test2 = Archive('test2', 2)
test3 = Archive('test3', 3)

# print(test1.text_archive)
# print(test3.text_archive)
# print(test2)
# print(f'{test1 = }')


"""
📌 Дорабатываем класс прямоугольник из прошлого семинара.
📌 Добавьте возможность сложения и вычитания.
📌 При этом должен создаваться новый экземпляр прямоугольника.
📌 При вычитании не допускайте отрицательных значений."""


class Rectangle:
    """Rectangle class. There are methods for comparing and finding the area and perimeter"""
    __slots__ = ('_length', '_width')

    def __init__(self, length, width=None):
        if length < 0:
            self._length = 1
        else:
            self._length = length
        if width is None or width < 0:
            self._width = length
        else:
            self._width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value > 0:
            self._length = value
        else:
            raise ValueError("the values must be greater than 0")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError("the values must be greater than 0")

    def length_rectangle(self):
        return (self._length + self._width) * 2

    def area_rectangle(self):
        return self._length * self._width

    def __add__(self, other):
        a = self._length + other.get_length
        b = self._width + other.get_width
        return Rectangle(a, b)

    def __sub__(self, other):
        a = self._length - other.length
        b = self._width - other.width
        if a < 0 or b < 0:
            return f"the operation is not possible"
        return Rectangle(a, b)

    def __eq__(self, other):
        return self.area_rectangle() == other.area_rectangle()

    def __ne__(self, other):
        return self.area_rectangle() != other.area_rectangle()

    def __gt__(self, other):
        return self.area_rectangle() > other.area_rectangle()

    def __ge__(self, other):
        return self.area_rectangle() <= other.area_rectangle()

    def __lt__(self, other):
        return self.area_rectangle() < other.area_rectangle()

    def __le__(self, other):
        return self.area_rectangle() >= other.area_rectangle()

    def __repr__(self):
        return f"Rectangle({self._length}, {self._width})"

    def __str__(self):
        return f"length = {self._length}\nwidth = {self._width}"


rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(3, 6)
rectangle3 = Rectangle(4)
# print(rectangle1 + rectangle2)
# print(rectangle1 - rectangle2)
# print(rectangle1 == rectangle2)
# print(rectangle1 != rectangle3)
# print(rectangle1 > rectangle2)
# print(rectangle1 < rectangle2)
# print(rectangle1 >= rectangle3)
# print(rectangle1 <= rectangle3)
