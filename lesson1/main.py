def tree():
    num = int(input("Сколько рядов у елки? "))
    count = 1
    while num > 0:
        print(' ' * num, "*" * count)
        count += 2
        num -= 1


def mul():
    print("Таблица умножения")

    num = 2
    count = 2

    while count < 10:
        while num < 10:
            print(f"{count} x {num} = {count * num}")
            num += 1
        count += 1
        num = 2
        print()

# tree()
# mul()
