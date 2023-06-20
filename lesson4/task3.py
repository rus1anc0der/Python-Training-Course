"""
Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""


class ATM:

    def __init__(self):
        self.sum: (int, float) = 0
        self.count_operation: int = 0

    def __str__(self) -> str:
        return f"На вашем счету {self.sum} у.е"

    # пополнить
    def to_up(self, value: (int, float)):
        if value % 50 == 0:
            self.sum += value
            self.sum_operation()
        else:
            print("Сумма пополнения должна быть кратна 50 у.е")
        self.tax()

    # снять
    def withdraw(self, value: (int, float)):
        if self.sum > value:
            if value % 50 == 0:
                if self.sum * 0.015 < 30:
                    self.sum -= value - 30
                elif self.sum * 0.015 > 600:
                    self.sum -= value - 600
                else:
                    self.sum -= value - (self.sum * 0.015)
            else:
                print("Сумма снятия должна быть кратна 50 y.e")
            self.sum_operation()
        else:
            print("Не достаточно средств на счету!")
        self.tax()

    # количество операций
    def sum_operation(self):
        self.count_operation += 1
        if self.count_operation % 3 == 0:
            self.sum += self.sum * 0.03
            print("Вам начислено бонусные 3% на ваш счет")

    # налог на богатство
    def tax(self):
        if self.sum > 5_000_000:
            self.sum -= self.sum * 0.1
            print("Вычтен налог на богатство 10% от текущего баланса")


atm = ATM()
list_operation: list = []
while True:
    print(f"\nМеню банкомата\n{'=' * 30}\n"
          + "1 - Пополнить\n"
          + "2 - Снять\n"
          + "3 - Баланс\n"
          + "4 - История операций\n"
          + "5 - Выйти\n"
          + "=" * 30)
    try:
        enter: int = int(input("Какую команду выполнить? --> "))
        match enter:
            case 1:
                value = int(input("Введите сумму для пополнения баланса --> "))
                atm.to_up(value)
                list_operation.append(f"Баланс пополнен на {value} y.e")

            case 2:
                value = int(input("Введите сумму для снятия --> "))
                atm.withdraw(value)
                list_operation.append(f"Снятие со счета {value} y.e")

            case 3:
                print(f"Ваш баланс {atm.sum}")

            case 4:
                for i in list_operation:
                    print(i)

            case 5:
                break

    except ValueError:
        print("Не верная команда!")
        continue
