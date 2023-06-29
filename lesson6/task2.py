"""Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь. []"""


# печать шахматной доски для визуального примера с точками, где находятся ферзи
def test():
    lst: list = [[0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0]]

    res = []
    print(*[f"{i} " for i in range(0, 9)])
    for enum, i in enumerate(range(len(lst)), start=1):
        print(enum, end='  ')
        for j in range(len(lst)):
            if lst[i][j] == 1:
                res.append(f"{i + 1}={j + 1}")
                print("♖", end='  ')
            else:
                print("-", end='  ')
        print()
    print(*res)
"""
Ферзи пересекаются если выполняется условие:
if одинаковая строка ( i )
if одинаковый столбец ( j )
if строка и столбец одновременно отличаются на n ( i + n and j + n )
"""
#                   lst[i][j]
checking_list: list = [[1, 3],
                       [2, 5],
                       [3, 2],
                       [4, 8],
                       [5, 1],
                       [6, 7],
                       [7, 4],
                       [8, 6]]


def checking_coordinates(lst: list) -> bool:
    count = 0
    for i in range(len(lst) - 1):
        while count < len(lst) - 1:
            if lst[i][0] == lst[count + 1][0] or lst[i][1] == lst[count + 1][1]:
                return False
            elif lst[i][0] - lst[count + 1][0] == lst[i][1] - lst[count + 1][1]:
                return False
            count += 1
        count = i + 1
    return True


if __name__ == "__main__":
    test()
    print(checking_coordinates(checking_list))