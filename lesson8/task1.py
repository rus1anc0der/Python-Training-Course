"""Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
-Для дочерних объектов указывайте родительскую директорию.
-Для каждого объекта укажите файл это или директория.
-Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
файлов и директорий."""
import os
import csv
import json
import pickle


def find_file(path):
    with(open("task1.csv", 'w', encoding='utf-8') as wcsv,
         open("task1.JSON", 'w', encoding='utf-8') as wjson,
         open('task1.pickle', 'wb') as wpickle):
        csv_write = csv.writer(wcsv, dialect='excel-tab', delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow(['dir_path', 'dir_name', 'file_name', 'size'])
        list_csv: list = []
        dict_json: dict = {}
        for dir_path, dir_name, file_name in os.walk(path):
            size = sum([os.path.getsize(i) for i, _, _ in os.walk(dir_path)])
            print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n{size = }\n')
            list_csv.append(
                [dir_path, dir_name, file_name, size])
            dict_json[f"{dir_path = }"] = [f"{dir_name = }", f"{file_name = }", f"{size = }"]
        pickle.dump(dict_json, wpickle)
        json.dump(dict_json, wjson, ensure_ascii=False, indent=2)
        csv_write.writerows(list_csv)


find_file('/Users/ruslanrustamov/Documents/Учеба/Python/ДЗ по курсу Python')
