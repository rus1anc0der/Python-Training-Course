'''
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
'''


def hex_decimal(value: int) -> str:
    res: str = ''
    while value > 0:
        if value % 16 == 10:
            res += 'a'
            value //= 16
        elif value % 16 == 11:
            res += 'b'
            value //= 16
        elif value % 16 == 12:
            res += 'c'
            value //= 16
        elif value % 16 == 13:
            res += 'd'
            value //= 16
        elif value % 16 == 14:
            res += 'e'
            value //= 16
        elif value % 16 == 15:
            res += 'f'
            value //= 16
        else:
            res += str(value % 16)
            value //= 16
    return res[::-1]


num = int(input("Введите число для перевода в шестнадцатеричную систему счисления: "))
print(f"0x{hex_decimal(num)}" == hex(num))
