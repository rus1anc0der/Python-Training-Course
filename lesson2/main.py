import math
import decimal
import cmath

"""
task 1
    Создайте несколько переменных разных типов.
    Проверьте к какому типу относятся созданные переменные.
"""
test_int: int = 1
test_float: float = 1.0
test_string: str = "Hello wold"
test_bool: bool = True
test_list: list = []
test_dict: dict = {}
test_tuple: tuple = ()

"""
task 2
    Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок. 
    Для каждого элемента в цикле выведите:
    ✔ порядковый номер начиная с единицы
    ✔ значение
    ✔ адрес в памяти
    ✔ размер в памяти
    ✔ хэш объекта
    ✔ результат проверки на целое число только если он положительный
    ✔ результат проверки на строку только если он положительный
"""
# data: list = [1, 1.0, "Hello wold", True, [], {}, ()]
#
# for i, val in enumerate(data, 1):
#     try:
#         print(f"{i}) \
#         Значение = {val}\n\
#         Адресс в памяти = {id(val)}\n\
#         Размер в пямяти = {val.__sizeof__()}\n\
#         Хэш обьекта = {hash(val)}")
#         if isinstance(val, int):
#             print("\t\tРезультат проверки на целое число = True")
#         if isinstance(val, str):
#             print("\t\tРезультат проверки на строку = True")
#     except TypeError:
#         print(f"{i})\
#         Значение = {val}\n\
#         Адресс в памяти = {id(val)}\n\
#         Размер в пямяти = {val.__sizeof__()}\n\
#         Хэш обьекта у типа list не определено")

"""
task3
✔ Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
✔ Функции bin и oct используйте для проверки своего результата, а не для решения.
"""


def is_bin(num: int) -> str:
    res: str = ''
    while num > 1:
        res += str(num % 2)
        num //= 2
    else:
        res += "1"
    return res[::-1]


def is_oct(num: int) -> str:
    res: str = ''
    while num >= 1:
        res += str(num % 8)
        num //= 8
    return res[::-1]


# num: int = int(input("Введите целое число: "))

# print(f"0b{is_bin(num)}" == bin(num))
# print(f"0o{is_oct(num)}" == oct(num))


"""
task4
✔ Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять не менее 42 знаков после запятой.
"""


def area_of_the_circle(value: (int, float, decimal)) -> list:
    if value < 1000:
        pi = decimal.Decimal(math.pi)
        decimal.getcontext().prec = 60
        radius = decimal.Decimal(value) / 2
        square = pi * pow(radius, 2)
        circumference_length = pi * decimal.Decimal(value)
        res = [square, circumference_length]
        return res
    else:
        print("Диаметр не должен превышать 1000")


print(area_of_the_circle(311))

"""
task5
✔ Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
✔ Используйте комплексные числа для извлечения квадратного корня.
"""


def quadratic_equations(a: int, b: int, c: int) -> list:
    res: list = []
    discriminant = pow(b, 2) - (4 * a * c)
    if discriminant > 0:
        x1 = (-1 * b - cmath.sqrt(discriminant)) / (2 * a)
        x2 = (-1 * b + cmath.sqrt(discriminant)) / (2 * a)
        res.append(x1)
        res.append(x2)
    elif discriminant == 0:
        x1 = (-1 * b) / 2 * a
        res.append(x1)
    return res


print(*quadratic_equations(1, -5, 6))
