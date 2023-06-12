'''
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного числа используйте код:
'''
from random import randint

# попытки
COUNT = 10
# Загаданное число
rnd = randint(0, 1001)

print(f"Угадайте число за {COUNT} попыток! ")
while COUNT > 0:
    try:
        num = int(input("ваше число: "))
        if num == rnd:
            print(f"Вы угадали!\nЗа {10 - COUNT} попыток")
            COUNT = 10
        elif num > rnd:
            print("Загаданное число меньше\n", f"Осталось {COUNT - 1} попыток")
        elif num < rnd:
            print("Загаданное число больше\n", f"Осталось {COUNT - 1} попыток")
        else:
            print("Вы не угадали :(")
        COUNT -= 1
    except ValueError:
        print("Введите число! ")
else:
    print('Игра закончена!')
