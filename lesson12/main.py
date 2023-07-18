"""
📌 Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
📌 Экземпляр должен запоминать последние k значений.
📌 Параметр k передаётся при создании экземпляра.
📌 Добавьте метод для просмотра ранее вызываемых значений и их факториалов.

📌 Доработаем задачу 1.
📌 Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл."""
import json
from lesson11 import main


class Factorial:
    _dict_instance = {}
    list_num = []

    def __init__(self, k, path_file):
        self.k = k
        self.path_file = path_file

    def read_instance(self):
        return self._dict_instance

    def _add_to_dict(self, num):
        if num in self._dict_instance:
            return self._dict_instance[num]
        value = 1
        for i in range(1, num + 1):
            value *= i
        self.list_num.append(num)
        self._dict_instance[num] = value
        return value

    def __call__(self, num):
        if len(self._dict_instance) < self.k:
            return self._add_to_dict(num)
        elif len(self._dict_instance) == self.k:
            self._dict_instance.pop(self.list_num[0])
            return self._add_to_dict(num)

    def __enter__(self):
        self.file = open(self.path_file, 'w', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        json.dump(self._dict_instance, self.file, indent=2)
        self.file.close()


#
# test1 = Factorial(5, 'Factorial.json')
# print(test1(1))
# print(test1(2))
# print(test1(3))
# print(test1(3))
# print(test1(5))
# print(test1(6))
# print(test1.read_instance())
# with Factorial(4, 'Factorial.json'):
#     print(test1(10))


"""
📌 Создайте класс-генератор.
📌 Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
📌 Если переданы два параметра, считаем step=1.
📌 Если передан один параметр, также считаем start=1."""


class GeneratorFactorial:

    def __init__(self, stop, start=1, step=1):
        self.stop = stop
        self.start = start
        self.step = step
        self.first = 1
        self.value = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.first < self.stop:
            self.value *= self.first
            self.first += 1
            if self.first >= self.start:
                return self.value
        raise StopIteration


# test2 = GeneratorFactorial(11, 5, 2)
# for i in test2:
#     print(i)


"""📌 Доработайте класс прямоугольник из прошлых семинаров.
📌 Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений(отрицательных)
📌 Используйте декораторы свойств."""
#
# test_rectangle = main.Rectangle(11, 22)
# print(test_rectangle.length)
# print(test_rectangle.width)
# test_rectangle.width = 10
# print(test_rectangle.width)
# test_rectangle.length = -5  # raise ValueError("the values must be greater than 0")
# print(test_rectangle.length)
# test_rectangle.width = -100  # raise ValueError("the values must be greater than 0")
# print(test_rectangle.width)


""" Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря __dict__.
📌 Изменяем класс прямоугольника.
📌 Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера."""


class Range:

    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError("The value must be an integer")
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"The values must be greater than {self.min_value}")
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f"The values must be less than {self.max_value}")


class Rectangle:
    """Rectangle class. There are methods for comparing and finding the area and perimeter"""
    __slots__ = ('_length', '_width')
    length = Range(1, 10)
    width = Range(1, 10)

    def __init__(self, length, width=None):
        self.length = length
        self.width = width

    def length_rectangle(self):
        return (self.length + self.width) * 2

    def area_rectangle(self):
        return self.length * self.width

    def __add__(self, other):
        a = self.length + other.length
        b = self.width + other.width
        return Rectangle(a, b)

    def __sub__(self, other):
        a = self.length - other.length
        b = self.width - other.width
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
        return f"Rectangle({self.length}, {self.width})"

    def __str__(self):
        return f"length = {self.length}\nwidth = {self.width}"


rectangle = Rectangle(2, 2)
rectangle.length = 3
print(rectangle)
rectangle2 = Rectangle(2, 2)
# rectangle2.width = 15  #ValueError: The values must be less than 10
print(rectangle2)
