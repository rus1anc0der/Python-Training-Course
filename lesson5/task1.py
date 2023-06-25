"""✔Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""


# /Users/ruslanrustamov/Documents/Учеба/Python/ДЗ по курсу Python/lesson1/main.py


def foo(abs_path: str) -> tuple:
    lst: list = abs_path.split('/')
    return '/'.join(lst[:-1]), *lst[-1:], lst[-1:][0].split('.')[1]


for _ in foo("/Users/ruslanrustamov/Documents/Учеба/Python/ДЗ по курсу Python/lesson1/main.py"):
    print(_)
