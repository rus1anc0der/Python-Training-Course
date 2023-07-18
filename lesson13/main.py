"""📌 Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор,
пока он не введёт целое или вещественное число.
📌 Обрабатывайте не числовые данные как исключения."""
import json


def func():
    while True:
        try:
            num = input('enter numbers ')
            try:
                num = int(num)
                return num
            except ValueError:
                num = float(num)
                return num
        except ValueError:
            print('try again')


# func()


"""📌 Создайте функцию аналог get для словаря.
📌 Помимо самого словаря функция принимает ключ и
значение по умолчанию.
📌 При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
📌 Реализуйте работу через обработку исключений."""


def get_dict(dictionary: dict, key, default=None):
    try:
        return dictionary[key]
    except KeyError:
        return default


test_dict = {'one': 1, 'two': 2}

# print(get_dict(test_dict, 'three'))


"""📌 Создайте класс с базовым исключением и дочерние классы- исключения:
○ ошибка уровня,
○ ошибка доступа."""


class MyException(Exception):

    def __str__(self):
        return f'no such user was found'


class LevelError(MyException):

    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def __str__(self):
        return f"your level {self.min_value} should be above {self.max_value}"


class AccessError(MyException):
    ...


"""
📌 Вспоминаем задачу из семинара 8 про сериализация данных, где в бесконечном цикле запрашивали имя, 
    личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
📌 Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
📌 Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей."""


class Users:

    def __init__(self, name: str, id_user: int, lvl_user: int):
        self.name = name
        self.id_user = int(id_user)
        self.lvl_user = int(lvl_user)

    def get_users(self):
        return self.name, self.id_user, self.lvl_user

    def __eq__(self, other):
        return all((self.id_user == other.id_user, self.name == other.name))

    def __hash__(self):
        return hash((self.name, self.id_user, self.lvl_user))

    def __str__(self):
        return f'name - {self.name}\n\tid - {self.id_user}\n\tlvl - {self.lvl_user}'


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


def parse_json(path_file):
    set_users = set()
    with open(path_file, 'r', encoding='utf-8') as f:
        dict_users = json.load(f)
    for keys, values in dict_users.items():
        for key, value in values.items():
            set_users.add((Users(value, key, keys)))
    return set_users


# func_JSON()
# set_user = parse_json('func.JSON')
# for i in set_user:
#     print(i.name)


"""📌 Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
📌 загрузка данных (функция из задания 4)
📌 вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте 
    магический метод проверки на равенство пользователей. Если такого пользователя нет, вызывайте исключение доступа. 
    А если пользователь есть, получите его уровень из множества пользователей.
📌 добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа."""


class ProjectBaseData:

    def __init__(self, path_file):
        self.set_users = self.load_json(path_file)

    def load_json(self, path_file):
        set_users = set()
        with open(path_file, 'r', encoding='utf-8') as f:
            dict_users = json.load(f)
        for keys, values in dict_users.items():
            for key, value in values.items():
                set_users.add((Users(value, key, keys)))
        return set_users

    def load_system(self):
        print('It is required to specify the user name and id')
        while True:
            try:
                load_name = input('name -> ')
                load_id = int(input('id -> '))
                for user in self.set_users:
                    if user.name == load_name and user.id_user == load_id:
                        return user.lvl_user
                else:
                    raise MyException
            except ValueError:
                print('Try again!\nThe name must contain the letters and the ID of the digit')
            except MyException as e:
                print(e)

    def add_users_to_DB(self):
        you_lvl = self.load_system()
        while True:
            try:
                new_user_name = input('enter the name of the new user -> ')
                new_user_id = int(input('id -> '))
                new_user_lvl = int(input('lvl ->'))
                if new_user_lvl > you_lvl:
                    raise LevelError(you_lvl, new_user_lvl)
                for user in self.set_users:
                    if new_user_id == user.id_user:
                        print("this value already exists , enter another one")
                        continue
                self.set_users.add(Users(new_user_name, new_user_id, new_user_lvl))
                break
            except LevelError as e:
                print(e, 'Try again!')
                continue
        return self.set_users


print(*ProjectBaseData('func.JSON').add_users_to_DB())
