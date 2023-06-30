"""✔ Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции."""
import random
import string
from random import randint, uniform
from pathlib import Path
import shutil


def write_random_numbers(file_name: str, lines: int):
    for i in range(lines):
        with open(file_name, 'a', encoding="utf-8") as f:
            int_num = randint(-1000, 1001)
            float_num = uniform(-1000, 1001)
            f.write(f"{int_num} / {float_num}\n")


# write_random_numbers("write_random_numbers.txt", 5)


"""✔ Напишите функцию, которая генерирует псевдоимена.
✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
✔ Полученные имена сохраните в файл."""


def generate_name():
    for _ in range(3):
        with open("generate_name.txt", 'a', encoding="utf-8") as f:
            rnd_name = ''
            for _ in range(random.randint(4, 8)):
                rnd_name += random.choice(string.ascii_letters)
            f.write(f"{rnd_name.capitalize()}\n")


# generate_name()


"""✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
    ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
    ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
✔ При достижении конца более короткого файла, возвращайтесь в его начало."""

"""✔ Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона."""


def create_file(path_file: str, extensions: str, min_len_name=6, max_len_name=30, min_byte=256, max_byte=4096,
                count_file=42):
    for obj in Path(Path().cwd()).iterdir():
        if path_file == str(obj):
            break
    else:
        Path(path_file).mkdir(parents=True)
    for _ in range(count_file):
        rnd_name = ''
        for i in range(min_len_name, max_len_name):
            rnd_name += random.choice(string.ascii_letters)
        with open(
                f"{path_file}/{rnd_name}.{extensions}",
                "wb") as f:
            f.write(bytearray(random.randint(min_byte, max_byte)))


# create_file("/Users/ruslanrustamov/Documents/Учеба/Python/ДЗ по курсу Python/lesson7/test", "txt")


"""✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи."""


def create_file_extensions(extensioins: list, count_file: list):
    for i, j in zip(extensioins, count_file):
        create_file("/Users/ruslanrustamov/Documents/Учеба/Python/ДЗ по курсу Python/lesson7/test", i, count_file=j)


create_file_extensions(["mp4", "mp3", "py", "jpg", "png", 'txt'], [2, 3, 4, 5, 6, 7])

"""✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
 ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён."""

"""✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки."""


def sort_file():
    extensoins_video: list = ["avi", "mp4", "mov", 'mkv']
    extensoins_text: list = ["txt", 'doc', 'docx']
    extensoins_pictures: list = ["jpg", 'png', 'gif']
    extensoins_audio: list = ['mp3', 'wav', 'flac']
    for obj in Path("/Users/ruslanrustamov/Documents/Учеба/Python/ДЗ по курсу Python/lesson7/test/").iterdir():
        *_, file_exten = str(obj).split('.')
        *_, file_name = str(obj).split('/')
        if file_exten in extensoins_video:
            shutil.move(obj, Path().cwd() / 'test' / "video")
        elif file_exten in extensoins_audio:
            shutil.move(obj, Path().cwd() / 'test' / 'audio')
        elif file_exten in extensoins_text:
            shutil.move(obj, Path().cwd() / 'test' / 'text')
        elif file_exten in extensoins_pictures:
            shutil.move(obj, Path().cwd() / 'test' / "pictures")


sort_file()
