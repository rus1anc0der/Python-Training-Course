"""📌 Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых
"""


class CheckName:

    def __init__(self, name: str = None):
        self.name = name

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, str) or not value.isalpha() or not value.istitle():
            raise TypeError("invalid name format")


class Student:
    name = CheckName()
    full_name = CheckName()

    def __init__(self, name, full_name):
        self.name = name
        self.full_name = full_name

    def __str__(self):
        return f'name - {self.name}\nfull name - {self.full_name}'


test = Student('Ruslan', "Rustamov")
test2 = Student('Ivan', 'ivanov')  # TypeError: invalid name format
test3 = Student('Petrov', 'Petr1')  # TypeError: invalid name format
