"""📌 Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
○ *умножения матриц"""


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

    def __str__(self):
        """print for users"""
        return f'{self.matrix}'

    def __repr__(self):
        """print for Developers"""
        result = ''
        for i in self.matrix:
            result += str(i)
        return f"Matrix({result})"


lst1, lst2, lst3, lst4, lst5 = [5, 3, 3, 0, 5], [3, 4, 6, 1, 5], [3, 4, 6, 1, 5], [4, 6, 8, 4, 1], [1, 9, 3, 7, 7]
test = Matrix(lst1, lst2, lst3, lst4, lst5)
test2 = Matrix(lst5, lst4, lst3, lst2, lst1)
test3 = test + test2
print(test3)

mal1, mal2, mal3, mal4, mal5 = [1, 2, 3], [4, 5, 6], [7, 8], [9, 1], [2, 3]
test4 = Matrix(mal1, mal2) * Matrix(mal3, mal4, mal5)
print(test4)
print(f"{test = }")
