from QuantumTools import *
import matplotlib.pyplot as plt

a = 10


def test_psi(x, n):
    return np.sqrt(2 / a) * np.sin(n * np.pi * x / a)


def h_1(x):
    c = 0
    return np.sin(x) + c


def second_order_perturbation_energy(hamiltonian_1, psi_0, E_0, bounds=None, n_upper=10):
    def integrand(x, left, right):
        product = psi_0(x, left).conjugate() * hamiltonian_1(x) * psi_0(x, right)
        return product
    if bounds is None:
        bounds = [-1 * np.inf, np.inf]

    # Returns psi_1 nth element
    psi_correction_1 = [0] * n_upper
    # Sum across n upto n_upper
    for n in range(1, n_upper):
        # Sum across m given fixed n
        temp_sum = 0
        for m in range(0, n_upper):
            if n != m:
                numerator = integrator(integrand, m, n, bounds=bounds)
                denominator = E_0[n] - E_0[m]
                if denominator == 0:
                    print('Opps')
                    return 'infinity'
                temp_sum += (numerator**2 / denominator)
        psi_correction_1[n] = temp_sum

    return psi_correction_1


if __name__ == '__main__':
    h_bar = 1
    mass = 1
    energy_list = []
    for i in range(0, 5):
        energy_list.append(i ** 2 * np.pi ** 2 * h_bar ** 2 / (2 * mass * a ** 2))
    print(second_order_perturbation_energy(h_1, test_psi, energy_list, bounds=[0, a], n_upper=5))
