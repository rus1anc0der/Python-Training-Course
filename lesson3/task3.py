"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один
допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
"""

bags_dict: dict = {
    'tent': 200,
    'sleeping_bag': 100,
    'dishes': 100,
    'flashlight': 200,
    'aid': 200,
    'cream': 100,
    'matches': 100,
}


def backpack(volume: int, bags: dict) -> list:
    lst: list = []
    for key, value in bags.items():
        if (volume - value) >= 0:
            lst.append(key)
            volume -= value
    return lst


print(backpack(500, bags_dict))
