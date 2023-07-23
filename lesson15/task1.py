""""Первое задание
Функция получает на вход текст вида: “1-й четверг ноября”, “3я среда мая” и т.п.
📌 Преобразуйте его в дату в текущем году.
📌 Логируйте ошибки, если текст не соответствует формату.
📌 Добавьте возможность запуска из командной строки.
📌 При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели,
    текущий день недели и/или текущий месяц.
📌 Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5.
Второе задание
📌 Возьмите любые 1-3 задачи из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
    Также реализуйте возможность запуска из командной строки с передачей параметров."""
import argparse
from datetime import datetime, date, time, timedelta
import logging


def logging_writer(func):
    def wrapper(*args, **kwargs):
        logging.basicConfig(filename='project.log.', filemode='w', encoding='utf-8', level=logging.INFO)
        logger = logging.getLogger()
        logger.info(f'\ntime - {datetime.now()}\narguments - {args, kwargs}\nname function - {func.__name__}\n'
                    f'result - {func(*args, **kwargs)}')

    return wrapper


@logging_writer
def convert_date(text: str) -> date:
    parse_text = text.split()
    year = datetime.now().year
    logging.basicConfig(filename='task1.log.', filemode='a', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger()
    list_str_month = ['января', "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября",
                      "ноября", "декабря"]
    list_int_month = [i for i in range(1, 13)]
    try:
        if parse_text[-1] in list_str_month:
            month = list_str_month.index(parse_text[-1]) + 1
        elif int(parse_text[-1]) in list_int_month:
            month = int(parse_text[-1])
        else:
            month = datetime.now().month
    except ValueError:
        logger.error('не верно указан месяц')
    list_str_weeks = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    list_int_weeks = [i for i in range(1, 8)]
    try:
        if parse_text[-2] in list_str_weeks:
            week = list_str_weeks.index(parse_text[-2])
        elif int(parse_text[-2]) in list_int_weeks:
            week = int(parse_text[-2])
        else:
            week = datetime.now().weekday()
    except ValueError:
        logger.error('не верно указан день недели')
    days = timedelta(weeks=float(parse_text[0].split('-')[0]) - 1)
    result = date(year, month, day=1)
    while True:
        if week != result.weekday():
            result += timedelta(days=1)
            continue
        break
    result += days
    return result


@logging_writer
def triangle(a: int, b: int, c: int):
    if a == b == c:
        return 'Треугольник равносторонний'
    elif a == b or b == c or a == c:
        return "Треугольник равнобедренный"
    else:
        return "Треугольник разносторонний"


def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


@logging_writer
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('numbers', metavar='N', type=str, nargs='*')
    args = parser.parse_args()
    args_func = ' '.join(list(map(str, args.numbers)))
    if args_func:
        print(convert_date(args_func))  # запуск через консоль
    else:
        print(convert_date('2-ой вторник января'))  # запуск через main
    triangle(1, 2, 3)
    print(fibonacci(10))


if __name__ == '__main__':
    main()
