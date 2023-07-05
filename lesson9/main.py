"""📌 Создайте функцию-замыкание, которая запрашивает два целых числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
📌 Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток."""
import json
import random
from functools import wraps
from typing import Callable
from random import randint


def func1(func: Callable) -> Callable[[], str]:
    def wrapper() -> str:
        while True:
            a = int(input('the number for guessing from 1 to 100 ->  '))
            b = int(input('number of attempts from 1 to 10 ->  '))
            if 1 > b < 10:
                b = random.randint(1, 10)
            elif 1 > a < 100:
                a = random.randint(1, 100)
            else:
                break
        for i in range(b):
            res = int(input("enter your number -> "))
            if res == a:
                return 'successfully :)'
        else:
            return 'you lose :('

    return wrapper


@func1
def func2():
    pass


# print(func2())

"""📌 Дорабатываем задачу 1.
📌 Превратите внешнюю функцию в декоратор.
📌 Он должен проверять входят ли переданные в функцию- угадайку числа в диапазоны [1, 100] и [1, 10].
📌 Если не входят, вызывать функцию со случайными числами из диапазонов."""

"""📌 Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, 
    который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
📌 Каждый ключевой параметр сохраните как отдельный ключ json словаря.
📌 Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
📌 Имя файла должно совпадать с именем декорируемой функции."""


def write_json(func: Callable):
    def wrapper(*args, **kwargs):
        with open(f"{func.__name__}.JSON", 'w', encoding='utf-8') as f:
            res = func(*args, **kwargs)
            json.dump(res, f, indent=2)

    return wrapper


@write_json
def func3(*args, **kwargs):
    dict_json: dict = {}
    for key, value in kwargs.items():
        dict_json[key] = value
    return dict_json


# func3(num1=1, num2=2)

"""📌 Создайте декоратор с параметром.
📌 Параметр - целое число, количество запусков декорируемой функции."""


def count(num: int = 1):
    def print_smile(func: Callable):
        def wrapper(*args, **kwargs):
            for _ in range(num):
                print(func(*args, **kwargs))

        return wrapper

    return print_smile


@count(10)
def func4():
    return ':)'


# func4()


"""
📌 Объедините функции из прошлых задач.
📌 Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
📌 Выберите верный порядок декораторов."""


def count(num: int = 1):
    def func5(func: Callable):
        res: list = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                res.append(func(*args, **kwargs))
            return res

        return wrapper

    return func5


def control_of_values(func: Callable):
    @wraps(func)
    def wrapper(a: int, b: int):
        if 1 > a or a > 100:
            b = random.randint(1, 100)
            print("control_of_values 'a'")
        if 1 > b or b > 10:
            a = random.randint(1, 10)
            print("control_of_values 'b'")
        return func(a, b)

    return wrapper


@count(2)
@control_of_values
def guess_the_number(a: int, b: int):
    """functions guess the number """
    for i in range(b):
        res = int(input("enter your number -> "))
        if res < a:
            print("number more, try else")
        elif res > a:
            print("number less, try else")
        else:
            return 'successfully :)'
    else:
        return 'you lose :('


a = int(input('the number for guessing from 1 to 100 ->  '))
b = int(input('number of attempts from 1 to 10 ->  '))
print(guess_the_number(a, b))

"""📌 Доработайте прошлую задачу добавив декоратор wraps в каждый из декораторов."""
