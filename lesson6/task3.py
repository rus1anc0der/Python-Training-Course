"""Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей
в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки."""
from task2 import *
from random import randrange, randint


def random_checking_list():
    count = 0
    while count < 4:
        random_numbers: list = [[randint(1, 9) for i in range(2)] for i in range(8)]
        if checking_coordinates(random_numbers):
            print(random_numbers)
            count += 1


random_checking_list()
