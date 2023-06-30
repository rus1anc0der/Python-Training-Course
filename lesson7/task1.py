"""Напишите функцию группового переименования файлов. Она должна:
    принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
    Принимать параметр количество цифр в порядковом номере.
    Принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога
    принимать параметр расширение конечного файла.
    Принимать диапазон сохраняемого оригинального имени. Например, для диапазона [3, 6] берутся буквы с 3 по 6
    из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано.
    Далее счётчик файлов и расширение."""
from pathlib import Path


def func(file_name: str, serial_number: int, original_extensions: str, end_file_extension: str, range_name: list):
    count = pow(10, serial_number)
    for i, obj in enumerate(Path().cwd().iterdir(), start=count):
        *_, extensions_file = str(obj).split('.')
        *_, name_file = str(obj).split('/')
        if extensions_file == original_extensions:
            print(Path(obj).rename(f"{name_file[range_name[0]:range_name[1]]}_{file_name}_{i}.{end_file_extension}"))


func("test_func", 2, 'py', "py", [3, 6])

