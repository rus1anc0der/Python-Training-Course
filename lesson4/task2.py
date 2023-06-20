"""
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
используйте его строковое представление.
"""


def my_func(**kwargs) -> dict:
    result: dict = {}
    for key, value in kwargs.items():
        if isinstance(key, (int, float, bool)):
            key = str(key)
        result[value] = key
    return result


print(my_func(математика=4, русский=5, физика=4))
