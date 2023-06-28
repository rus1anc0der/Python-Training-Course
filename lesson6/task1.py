"""Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку. []"""
import sys


def check_date(list_date: str) -> bool:
    if leap_year(list_date):
        if int(list_date[0]) > 29 or int(list_date[1]) > 12:
            return False
        return True
    else:
        if int(list_date[0]) > 28 or int(list_date[1]) > 12:
            return False
        return True


def leap_year(list_date: str) -> bool:
    if int(list_date[2]) % 4 == 0:
        if int(list_date[2]) % 100 == 0 and int(list_date[2]) % 400 == 0:
            return False
        return True
    return False


user_input_date = sys.argv
user_input_date.pop(0)
print(check_date(user_input_date))
