# """
# task1
# ✔ Вручную создайте список с целыми числами, которые повторяются. Получите новый список,
#     который содержит уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.
# """
#
# lst: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7, 6]
# set_lst: list = list(set(lst))
# print(set_lst)
#
# lst: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7, 6]
# for i in lst:
#     if lst.count(i) > 1:
#         lst.pop(i)
# print(lst)
#
# """
# task2
# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях
# """
#
# data: str = input("Введите что нибудь -> ")
#
#
# def is_apper(string: str) -> bool:
#     for char in string:
#         if char.isupper():
#             return True
#
#
# try:
#     if data.isdigit():
#         if int(data) > 0:
#             print("Целое положительное число")
#     elif isinstance(float(data), float):
#         print("Вещественное положительное или отрицательное число")
# except ValueError:
#     if data.isascii():
#         if is_apper(data):
#             print(data.lower())
#         else:
#             print(data.lower())
#
#
# """
# task3
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где: ключ — тип элемента,
# значение — список элементов данного типа.
# """
#
# test_tuple: tuple = (1, 25, 29.32, 1.1, True, False,  "String", "Dict", [], [1, 2, 4])
# test_dict: dict = {}
# for value in test_tuple:
#     test_dict[type(value)] = [i for i in test_tuple if type(value) == type(i)]
#
# print(test_dict)
#
# """
# task4
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.
# """
#
# test_list: list = [1, 2, 2, 33, 1, 2, 0, 33]
# for i in test_list:
#     if test_list.count(i) == 2:
#         test_list.remove(i)
#         test_list.remove(i)
#
# print(test_list)
#
#
#
# """
# task5
# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.
# """
#
#
#
#
# """
# task6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.
# """
#
# user_input: str = input("Введите текст -> ")
# sort: list = sorted(user_input.split())
# max_len: int = 0
# for i in sort:
#     if max_len < len(i):
#         max_len = len(i)
# for i, num in enumerate(sort, 1):
#     print(f"{i} {num:>{max_len}}")
#
#
# """
# task7
# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# ✔ Обратите внимание на порядок ключей. Объясните почему они совпадают
# или не совпадают в ваших решениях.
# """
#
# user_input2: str = input("Введите строку -> ")
# count_char: int = 0
# result_dict: dict = {}
# for i in user_input2:
#     for k in user_input2:
#         if i == k:
#             count_char += 1
#     result_dict[i] = count_char
#     count_char = 0
#
# print(result_dict)
#
#
# """
# task8
# ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
#     Ответьте на вопросы:
#     1✔ Какие вещи взяли все три друга
#     2✔ Какие вещи уникальны, есть только у одного друга
#     3✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
#     ✔ Для решения используйте операции
#     с множествами. Код должен расширяться на любое большее количество друзей.
# """

bags: dict = {
    'Anna': ("meat", "mirror", "T-shirt"),
    'Kirill': ("T-shirt", "sneakers", "hairbrush"),
    'Ivan': ("meat", "mirror", "sneakers", 'T-shirt'),
}


def item1(dict_values: dict) -> set:
    result: set = set()
    for i in dict_values.values():
        result = set(i)
        for k in dict_values.values():
            result &= set(k)
        break
    return result


def item2(dict_values: dict) -> set:
    result: set = set()
    for i in dict_values.values():
        result = set(i)
        for k in dict_values.values():
            if i == k:
                continue
            else:
                result -= set(k)
        break
    return result


def item3(dict_values: dict) -> set:
    pass


print(item1(bags))
print(item2(bags))
