"""
task6
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
✔ Любое действие выводит сумму денег
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
while True:
    print(f"\nМеню банкомата\n{'=' * 30}\n"
          + "1 - Пополнить\n"
          + "2 - Снять\n"
          + "3 - Баланс\n"
          + "4 - Выйти\n"
          + "=" * 30)
    try:
        enter: int = int(input("Какую команду выполнить? --> "))
        match enter:
            case 1:
                value = int(input("Введите сумму для пополнения баланса --> "))
                atm.to_up(value)

            case 2:
                value = int(input("Введите сумму для снятия --> "))
                atm.withdraw(value)

            case 3:
                print(f"Ваш баланс {atm.sum}")

            case 4:
                break

    except ValueError:
        print("Не верная команда!")
        continue
