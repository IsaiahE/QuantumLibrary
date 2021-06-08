# Integrator for Quantum Perturbation functions require two inputs
import scipy.integrate as integrate
import numpy as np

a = 1


def test_psi(x, n):
    return np.sqrt(2 / a) * np.sin(n * np.pi * x / a)


def hamiltonian_1(x):
    return -(x - 1 / 2) ** 2 + 10


def integrand_nm(x, n, m):
    product = test_psi(x, n).conjugate() * hamiltonian_1(x) * test_psi(x, m)
    return product


def integrator(function, left_state, right_state, bounds=None, N=100000):
    """Function to integrate Psi* H Psi functions require three inputs x, n, m
    function - total function to be integrated
    left_state - integer
    right_state - integer
    bounds - default - [-1000, 1000]
    """
    if bounds is None:
        bounds = [-1000, 1000]
    area = 0
    delta_x = (bounds[1] - bounds[0]) / N
    for i in range(0, N):
        height = function(bounds[0] + (i + .5) * delta_x, left_state, right_state)
        rectangle = height * delta_x
        area += rectangle
    return area


class Matrix:

    """Row/ Column starts at 0, 0
    Does not check if lengths match up

    Matrix Multiplication not complete"""

    def __init__(self, rows=0, columns=0, name=None):
        self.total_rows = rows
        self.total_columns = columns
        self.name = name
        self.elements = [[0] * (self.total_columns + 1)] * (self.total_rows + 1)

    def get_value(self, row, column):
        return self.elements[row][column]

    def make_value(self, row, column, value):
        self.elements[row][column] = value

    def check_row(self):
        return len(self.elements)

    def check_column(self):
        return len(self.elements[0])

    def get_row(self, row):
        return self.elements[row]

    def get_column(self, column):
        column_to_return = []
        for row_cycle in range(len(self.elements)):
            column_to_return.append(self.elements[row_cycle][column])
        return column_to_return

    def print_matrix(self):
        print(self.name)
        for row_cycle in range(len(self.elements)):
            for column_cycle in range(len(self.elements[row_cycle])):
                if column_cycle < len(self.elements[row_cycle]) - 1:
                    print(' ' + str(self.elements[row_cycle][column_cycle]) + ' ', end='')
                else:
                    print(' ' + str(self.elements[row_cycle][column_cycle]) + ' ')

    def matrix_multiply(self, other_matrix):
        max_row = 0
        max_column = 0
        if max_row < self.total_rows:
            max_row = self.total_rows
        if max_row < other_matrix.check_row():
            max_row = other_matrix.check_row()
        if max_column < self.total_columns:
            max_column = self.total_columns
        if max_column < other_matrix.check_column():
            max_column = other_matrix.check_column()
        matrix_to_return = [[0] * (other_matrix.get_column() + 1)]*(self.total_rows + 1)
        vector_dic = dict()
        for n in range(len(self.total_columns)):
            vector_dic[f'{n}'] = self.get_column(n)
        temp_vec = [0] * self.total_rows
        for column_cycle in other_matrix:
            dummy_var = 0
            for i in column_cycle:
                temp_vec += vector_dic[dummy_var] * i
                dummy_var += 1



            return matrix_to_return


if __name__ == '__main__':
    matrixy = Matrix(2, 2, 'matrixy')
    vectory = Matrix(2, 0, 'vectory')
    for i in range(0, 3):
        for j in range(0, 3):
            matrixy.make_value(i, j, i + j)
    for i in range(0, 2):
        vectory.make_value(i, 0, i)
        
    matrixy.print_matrix()
    vectory.print_matrix()

    print(matrixy.matrix_multiply(vectory))
