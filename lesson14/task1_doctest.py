"""📌 Возьмите 1-3 задачи из тех, что были на прошлых
семинарах или в домашних заданиях.
📌 Напишите к ним тесты.
📌 2-5 тестов на задачу в трёх вариантах:
○ doctest,
○ unittest,
○ pytest."""
import doctest


class Matrix:
    """Matrix class with methods:
                                 Print output,
                                 comparisons,
                                 additions,
                                 matrix multiplications"""

    def __init__(self, *args):
        self.matrix = [i for i in args]
        self.row = len(self.matrix)
        self.column = len(self.matrix[0])

    def __add__(self, other):
        """
        >>> Matrix([1]) + Matrix([2])
        Matrix([3])
        """
        """additions"""
        if self.column == other.column and self.row == other.column:
            result = []
            for row, i in enumerate(self.matrix):
                result.append([])
                for col, j in enumerate(i):
                    result[row].append(self.matrix[row][col] + other.matrix[row][col])
            return Matrix(*result)
        return f"addition is not possible"

    def __mul__(self, other):
        """
        >>> Matrix([1]) * Matrix([2])
        Matrix([2])
        """
        """matrix multiplications"""
        if self.column == other.row:
            result = []
            temp = 0
            for row in range(self.row):
                result.append([])
                for col in range(other.column):
                    for enum in range(self.column):
                        temp += self.matrix[row][enum] * other.matrix[enum][col]
                    result[row].append(temp)
                    temp = 0
            return Matrix(*result)
        return f"matrix multiplication is not possible"

    def print_matrix(self):
        """Print output"""
        for i in self.matrix:
            for j in i:
                print(j, end='  ')
            print()

    def __eq__(self, other):
        """method comparisons"""
        if self.column == other.column and self.row == other.row:
            for row in range(self.row):
                for col in range(self.column):
                    if self.matrix[row][col] == other.matrix[row][col]:
                        continue
                    else:
                        return False
            return True

        return False

    def __str__(self):
        """print for users"""
        return f'{self.matrix}'

    def __repr__(self):
        """print for Developers"""
        result = ''
        for i in self.matrix:
            result += str(i)
        return f"Matrix({result})"
def func1(a: int, b: int, c: int):
    """
    >>> func1(1, 2, 3)
    'Треугольник разносторонний'
    >>> func1(2, 2, 2)
    'Треугольник равносторонний'
    >>> func1(2, 2 ,3)
    'Треугольник равнобедренный'
    """
    if a == b == c:
        return "Треугольник равносторонний"
    elif a == b or b == c or a == c:
        return "Треугольник равнобедренный"
    else:
        return "Треугольник разносторонний"


def func2(number) -> bool:
    """
    >>> func2(42)
    False
    >>> func2(73)
    True
    """
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def main():
    while True:
        try:
            a, b, c = map(int, input('Введите стороны треугольника через запятую-> ').split())
            if a > (b + c) or b > (a + c) or c > (a + b):
                raise ValueError("Треугольника с такими сторонами не существует")
            print(func1(a, b, c))
            break
        except ValueError as e:
            continue
    while True:
        try:
            number = int(input("Введите число в диапазоне от 0 до 100 000 :  "))
            if number < 0 or number > 100_000:
                raise ValueError("Число не входит в диапазон!")
            print(func2(number))
            break
        except ValueError as e:
            continue


if __name__ == "__main__":
    doctest.testmod(verbose=True)

