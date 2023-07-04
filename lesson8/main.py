"""📌 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
📌 Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
📌 Имена пишите с большой буквы.
📌 Каждую пару сохраняйте с новой строки."""
import json
import csv
import pickle
from pathlib import Path


def write_text_JSON():
    list_name: list = []
    list_numbers: list = []
    with (open("/Users/ruslanrustamov/Documents/Учеба/Python/ДЗ по курсу Python/lesson7/create_name_number.txt",
               "r", encoding='utf-8') as cnn,
          open("name_number.JSON", 'w') as nnJSON):
        for i in cnn:
            for j in i.split('\n')[0].split('-'):
                if j.isalpha():
                    list_name.append(j)
                else:
                    list_numbers.append(j)
        name_number_JSON: dict = {}
        for name, number in zip(list_name, list_numbers):
            name_number_JSON[name.capitalize()] = number
        json.dump(name_number_JSON, nnJSON, indent=2)
        print(list_numbers)
        print(list_name)


# write_text_JSON()

"""📌 Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
📌 После каждого ввода добавляйте новую информацию в JSON файл.
📌 Пользователи группируются по уровню доступа.
📌 Идентификатор пользователя выступает ключём для имени.
📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
📌 При перезапуске функции уже записанные в файл данные должны сохраняться."""


def func_JSON():
    with open("func.JSON", 'a', encoding="utf-8") as funcJ:
        dict_lvl_JSON: dict = {}
        res = True
        while res:
            dict_id_JSON: dict = {}
            input_name: str = input("Ваше имя -> ")
            if input_name == 'end':
                res = False
                continue
            while True:
                input_id: int = int(input("Личный идентификатор -> "))
                if input_id in dict_id_JSON.keys():
                    print("Такой идентификатор уже существует , введите другой")
                else:
                    break
            while True:
                input_lvl: int = int(input("Уровень доступа -> "))
                if 0 > input_lvl > 8:
                    print('Уровень доступа должен быть от 1 до 7')
                else:
                    break
            dict_id_JSON[input_id] = input_name
            dict_lvl_JSON[input_lvl] = dict_id_JSON
        json.dump(dict_lvl_JSON, funcJ, ensure_ascii=False, indent=2, sort_keys=True)


# func_JSON()

"""📌 Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV."""


def func_CSV():
    with (open("func.JSON", 'r', encoding='utf-8') as f,
          open("func_CSV.csv", "w", newline='', encoding='utf-8') as f2):
        write_list: list = []
        json_file = json.load(f)
        print(json_file)
        csv_write = csv.writer(f2, dialect='excel', delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow(['Lvl', 'Name', 'ID'])
        for keys, values in json_file.items():
            for key, value in values.items():
                write_list.append([key, value, keys])
        csv_write.writerows(write_list)


# func_CSV()


"""📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
📌 Дополните id до 10 цифр незначащими нулями.
📌 В именах первую букву сделайте прописной.
📌 Добавьте поле хеш на основе имени и идентификатора.
📌 Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
📌 Имя исходного и конечного файлов передавайте как аргументы функции."""


def csv_to_JSON(csv, JSON):
    with (open(csv, 'r') as csv_read,
          open(JSON, 'w', encoding='utf-8') as JSON_writer):
        dict_json: dict = {}
        for enum, line in enumerate(csv_read):
            dict_csv_line: dict = {}
            line = line.split('\n')[0].split(',')
            print(line)
            if enum != 0:
                dict_csv_line[line[0]] = f"{len(line[1]) + (10_000_000_000 - int(line[2]))}"
                dict_json[enum] = dict_csv_line
        json.dump(dict_json, JSON_writer, ensure_ascii=False, indent=2)


# csv_to_JSON('func_CSV.csv', 'csv_to_JSON.JSON')


"""📌 Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых 
pickle файлов."""


def func_pickle():
    for enum, path_file in enumerate(Path(Path.cwd()).iterdir()):
        *_, file = str(path_file).split('.')
        if file == 'JSON':
            with (open(path_file, 'r') as r_json,
                  open(f'pickle{enum}.pickle', 'wb') as write_pickle):
                pickle.dump(r_json.read(), write_pickle)


# func_pickle()


"""📌 Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
📌 Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
📌 Функция должна извлекать ключи словаря для заголовков столбца из переданного файла."""


def pickle_to_csv():
    with (open("pickle5.pickle", 'rb') as rp,
          open('pickle_to_csv.csv', "w", encoding='utf-8') as ptc):
        new_dict: dict = json.loads(pickle.load(rp))
        csv_write = csv.DictWriter(ptc, fieldnames=[str(i) for i in new_dict.keys()], dialect='excel-tab',
                                   quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        csv_write.writerows([new_dict])


# pickle_to_csv()


"""📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
📌 Распечатайте его как pickle строку."""

with open("pickle_to_csv.csv", 'r') as p_read:
    for line in p_read:
        print(pickle.dumps(line, protocol=pickle.DEFAULT_PROTOCOL))
