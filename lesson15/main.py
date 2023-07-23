"""📌 Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
📌 Например отлавливаем ошибку деления на ноль."""
import argparse
from datetime import datetime, date, time, timedelta
import logging


def func1(val):
    logging.basicConfig(filename='project.log.', filemode='w', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger('start')
    try:
        return 100 / val
    except ValueError:
        logger.warning('ValueError')
    except ZeroDivisionError:
        logger.warning('ZeroDivisionError')


"""📌 На семинаре про декораторы был создан логирующий декоратор. 
    Он сохранял аргументы функции и результат её работы в файл.
📌 Напишите аналогичный декоратор, но внутри используйте модуль logging.

📌 Доработаем задачу 2.
📌 Сохраняйте в лог файл раздельно:
○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат."""


def func2(func):
    def wrapper(*args, **kwargs):
        logging.basicConfig(filename='project.log.', filemode='w', encoding='utf-8', level=logging.INFO)
        logger = logging.getLogger('start')
        logger.info(f'\ntime - {datetime.now()}\narguments - {args, kwargs}\nname function - {func.__name__}\n'
                    f'result - {func(*args, **kwargs)}')

    return wrapper


@func2
def func3(val):
    return [i for i in range(val)]


"""📌 Функция получает на вход текст вида: “1-й четверг ноября”, “3- я среда мая” и т.п.
📌 Преобразуйте его в дату в текущем году.
📌 Логируйте ошибки, если текст не соответствует формату.
📌 Добавьте возможность запуска из командной строки.
📌 При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели,
    текущий день недели и/или текущий месяц.
📌 *Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые,
т.е не мая, а 5."""


def func4(text: str) -> date:
    parse_text = text.split()
    year = datetime.now().year
    logging.basicConfig(filename='project.log.', filemode='w', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger('start')
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


def main():
    # print(func1(100))
    # func3(10)
    parser = argparse.ArgumentParser()
    parser.add_argument('numbers', metavar='N', type=str, nargs='*')
    args = parser.parse_args()
    args_func = ' '.join(list(map(str, args.numbers)))
    if args_func:
        print(func4(args_func))  # запуск через консоль
    else:
        print(func4('2-ой вторник января'))


if __name__ == '__main__':
    main()
