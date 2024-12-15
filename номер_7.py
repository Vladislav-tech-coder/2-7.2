class Matrix:
    def __init__(self, data):
        """Инициализатор матрицы."""
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    @classmethod
    def from_file(cls, filename):
        """Инициализатор матрицы из файла."""
        with open(filename, 'r') as file:
            data = [list(map(float, line.split())) for line in file]
        return cls(data)

    def __add__(self, other):
        """Сложение двух матриц."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны иметь одинаковые размеры для сложения.")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other):
        """Умножение матрицы на число или умножение двух матриц."""
        if isinstance(other, (int, float)):
            result = [[self.data[i][j] * other for j in range(self.cols)] for i in range(self.rows)]
            return Matrix(result)
        elif isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Число столбцов первой матрицы должно совпадать с числом строк второй матрицы.")
            result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for
                      i in range(self.rows)]
            return Matrix(result)
        else:
            raise TypeError("Умножение возможно только с числом или другой матрицей.")

    def transpose(self):
        """Транспонирование матрицы."""
        result = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(result)

    def determinant(self):
        """Вычисление определителя матрицы (для квадратных матриц)."""
        if self.rows != self.cols:
            raise ValueError("Определитель можно вычислить только для квадратных матриц.")

        if self.rows == 1:
            return self.data[0][0]
        elif self.rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]

        det = 0
        for c in range(self.cols):
            minor = self.get_minor(0, c)
            det += ((-1) ** c) * self.data[0][c] * minor.determinant()
        return det

    def get_minor(self, row, col):
        """Получение минора матрицы."""
        minor = [r[:col] + r[col + 1:] for i, r in enumerate(self.data) if i != row]
        return Matrix(minor)

    def to_file(self, filename):
        """Запись матрицы в файл."""
        with open(filename, 'w') as file:
            for row in self.data:
                file.write(' '.join(map(str, row)) + '\n')

    def __str__(self):
        """Строковое представление матрицы."""
        return '\n'.join([' '.join(map(str, row)) for row in self.data])


# Пример использования
if __name__ == "__main__":
    # Инициализация матрицы из файла
    matrix_a = Matrix.from_file('matrix_a.txt')
    matrix_b = Matrix.from_file('matrix_b.txt')

    # Сложение матриц
    matrix_sum = matrix_a + matrix_b
    print("Сумма матриц:\n", matrix_sum)

    # Умножение матрицы на число
    matrix_scaled = matrix_a * 2
    print("Матрица, умноженная на 2:\n", matrix_scaled)

    # Умножение матриц
    matrix_product = matrix_a * matrix_b
    print("Произведение матриц:\n", matrix_product)

    # Транспонирование матрицы
    matrix_transposed = matrix_a.transpose()
    print("Транспонированная матрица:\n", matrix_transposed)

    # Вычисление определителя
    det_a = matrix_a.determinant()
    print("Определитель матрицы A:", det_a)

    # Запись результата в файл
    matrix_sum.to_file('result.txt')
    