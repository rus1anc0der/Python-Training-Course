"""📌 Возьмите 1-3 задачи из тех, что были на прошлых
семинарах или в домашних заданиях. Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например, нельзя создавать прямоугольник со сторонами отрицательной длины
"""


class LimitException(Exception):

    def __init__(self, val: int):
        self.value = val

    def __str__(self):
        return f'the limit has been exceeded , it is impossible to deposit more than {self.value}'


class ATM:
    LIMIT = 150_000

    def __init__(self):
        self.sum: (int, float) = 0
        self.count_operation: int = 0

    def __str__(self) -> str:
        return f"На вашем счету {self.sum} у.е"

    # пополнить
    def to_up(self, value: (int, float)) -> bool:
        if value % 50 == 0:
            self.sum += value
            self.sum_operation()
            self.tax()
            return True
        else:
            print("Сумма пополнения должна быть кратна 50 у.е")
            return False

    # снять
    def withdraw(self, value: (int, float)) -> bool:
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
            self.tax()
            return True
        else:
            print("Не достаточно средств на счету!")
            return False

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
                while True:
                    try:
                        value = int(input("Введите сумму для пополнения баланса --> "))
                        if value > ATM.LIMIT:
                            raise LimitException(ATM.LIMIT)
                        break
                    except LimitException as e:
                        print(e, 'Try again!')
                if atm.to_up(value):
                    list_operation.append(f"Баланс пополнен на {value} y.e")

            case 2:
                while True:
                    try:
                        value = int(input("Введите сумму для снятия --> "))
                        if value > ATM.LIMIT:
                            raise LimitException(ATM.LIMIT)
                        break
                    except LimitException as e:
                        print(e)
                if atm.withdraw(value):
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
