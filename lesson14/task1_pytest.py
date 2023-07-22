"""📌 Возьмите 1-3 задачи из тех, что были на прошлых
семинарах или в домашних заданиях.
📌 Напишите к ним тесты.
📌 2-5 тестов на задачу в трёх вариантах:
○ doctest,
○ unittest,
○ pytest."""
import pytest


def func1(a: int, b: int, c: int):
    if a == b == c:
        return "Треугольник равносторонний"
    elif a == b or b == c or a == c:
        return "Треугольник равнобедренный"
    else:
        return "Треугольник разносторонний"


def func2(number) -> bool:
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def main():
    while True:
        try:
            a, b, c = map(int, input('Введите стороны треугольника через запятую-> ').split())
            if a > (b + c) or b > (a + c) or c > (a + b):
                raise ValueError("Треугольника с такими сторонами не существует")
            print(func1(a, b, c))
            break
        except ValueError as e:
            continue
    while True:
        try:
            number = int(input("Введите число в диапазоне от 0 до 100 000 :  "))
            if number < 0 or number > 100_000:
                raise ValueError("Число не входит в диапазон!")
            print(func2(number))
            break
        except ValueError as e:
            continue


def test_func1_1():
    assert func1(1, 2, 3) == "Треугольник разносторонний"


def test_func1_2():
    assert func1(2, 2, 2) == "Треугольник равносторонний"


def test_func1_3():
    assert func1(2, 2, 3) == "Треугольник равнобедренный"


if __name__ == "__main__":
    pytest.main()
