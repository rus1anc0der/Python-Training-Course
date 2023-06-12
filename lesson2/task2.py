'''
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
'''
import fractions


def my_func_sum(s1: str, s2: str) -> list:
    res: list = []
    s1 = [int(i) for i in s1.split("/")]
    s2 = [int(i) for i in s2.split("/")]
    if s1[1] == s2[1]:
        res.append(s1[0] + s2[0])
    else:
        temp = s1[1]
        s1[0] *= s2[1]
        s1[1] *= s2[1]
        s2[0] *= temp
        s2[1] *= temp
        res.append(s1[0] + s2[0])
    res.append(s1[1])
    return res


def my_func_mull(s1: str, s2: str) -> list:
    res: list = []
    s1 = [int(i) for i in s1.split("/")]
    s2 = [int(i) for i in s2.split("/")]
    res.append(s1[0] * s2[0])
    res.append(s1[1] * s2[1])
    return res


result_sum = "/".join(map(str, my_func_sum('2/9', '1/5')))
result_mull = "/".join(map(str, my_func_mull('2/9', '1/5')))
print(result_sum, result_mull)
print(fractions.Fraction(2, 9) + fractions.Fraction(1, 5), fractions.Fraction(2, 9) * fractions.Fraction(1, 5))
