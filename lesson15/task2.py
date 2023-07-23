import argparse
import logging


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


def main():
    logging.basicConfig(filename='task2.log.', filemode='a', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger()
    parser = argparse.ArgumentParser()
    parser.add_argument('numbers', metavar='N', type=int, nargs='*')
    args = parser.parse_args()
    if args.numbers:
        logger.info(f'result fibonacci - {fibonacci(*args.numbers)}')
        # logger.info(f'result triangle - {triangle(*args.numbers)}')
    else:
        logger.info(f'result fibonacci - {fibonacci(10)}')
        logger.info(f'result triangle - {triangle(10, 10, 10)}')


if __name__ == "__main__":
    main()
