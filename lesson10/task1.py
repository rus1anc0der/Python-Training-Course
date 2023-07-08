"""📌 Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
📌 Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
Задачи должны решаться через вызов методов экземпляра."""
import csv
import json

from main import Fish


class Factory(Fish):
    salmon = Fish("salmon", "ocean")

    def __init__(self, name, living_environment, color):
        super().__init__(name, living_environment)
        self.color = color


# Factory.salmon.all_info()


class Serialization:

    def write_json(self, path_file, dict_for_write):
        with open(path_file, 'w', encoding='utf-8') as f:
            json.dump(dict_for_write, f, indent=2)


Serialization().write_json('json.JSON', {1: '1', 2: '2'})
