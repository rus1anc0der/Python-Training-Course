"""
Напишите функцию для транспонирования матрицы
"""


def transpose_matrix(matrix):
    # Получаем количество строк и столбцов
    rows = len(matrix)
    cols = len(matrix[0])

    # Создаем новую матрицу с размерами столбцов и строк и заполняем нулями
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    # Заполняем новую матрицу значениями из исходной матрицы
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


matrix1: list = [[1, 2, 3], [4, 5, 6]]
print(transpose_matrix(matrix1))
