from math import factorial
import numpy as np


def legengre():
    y = 0


def print_hydrogen_stationary_state(n=1, l=0, m=0):
    coef_psi = np.sqrt((2/n)**3*factorial(n-l-1)/(factorial(n + l)*2*n))
    first = (2/n)**3
    second = factorial(n - l -1)
    third = 2*n*factorial(n + l)

    print(f'sqrt(({str(first)}/a^3)({str(second)}/{str(third)})) * e^(-r/{n}a) * (2r/{n}a)^{l}')


if __name__ == '__main__':
    print_hydrogen_stationary_state(n=2, l=1, m=0)
