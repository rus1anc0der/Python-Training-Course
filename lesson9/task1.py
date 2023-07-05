"""📌 Напишите следующие функции:
○ Нахождение корней квадратного уравнения
○ Генерация csv файла с тремя случайными числами в каждой строке.
100-1000 строк.
○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл."""
import csv
import json
import random
from math import sqrt


def read_csv(func):
    def wrapper(*args, **kwargs):
        with open("task1.csv", "r", encoding='utf-8') as f:
            for enum, line in enumerate(f):
                if enum != 0:
                    line = line.split('\n')[0].split(',')
                    line = [int(i) for i in line]
                    print(func(*line))

    return wrapper


def write_json(func):
    dict_json: dict = {}

    def wrapper(*args, **kwargs):
        with open("task1.json", 'w', encoding='utf-8') as f:
            dict_json[str(args)] = func(*args)
            json.dump(dict_json, f, indent=6)

    return wrapper


@read_csv
@write_json
def quadratic_equation(a: int, b: int, c: int):
    discriminant = b ** 2 - 4 * a * c
    try:
        if discriminant > 0:
            x1 = (-b + sqrt(discriminant)) / (2 * a)
            x2 = (-b - sqrt(discriminant)) / (2 * a)
        elif discriminant == 0:
            x1 = (-b + sqrt(discriminant)) / (2 * a)
            x2 = None
        else:
            return "no solution"
    except ZeroDivisionError:
        return "no solution"
    return x1, x2


def create_csv():
    with open("task1.csv", 'w', encoding='utf-8') as f:
        numbers = [[random.randint(-100, 100) for i in range(3)] for j in range(100, 1000)]
        csv_write = csv.writer(f, dialect='excel', delimiter=',', quotechar=' ', quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writerow(['a', 'b', 'c'])
        csv_write.writerows(numbers)


# create_csv()
quadratic_equation()
