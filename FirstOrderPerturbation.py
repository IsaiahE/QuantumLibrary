from QuantumTools import *
import matplotlib.pyplot as plt

a = 10


def test_psi(x, n):
    return np.sqrt(2 / a) * np.sin(n * np.pi * x / a)


def h_1(x):
    c = 0
    return np.sin(x) + c


def first_order_perturbation_energy(hamiltonian_1=lambda x: 0, psi_0=lambda x, n: 0, bounds=None, left_state=1):
    """Calculates and returns the first order correction to the energy for various states's
        requires perturbation to hamiltonian, the unpeterbed Psi, and the energy state left_state wanted
    """
    right_state = left_state

    def integrand(x, left, right):
        product = psi_0(x, left).conjugate() * hamiltonian_1(x) * psi_0(x, right)
        return product

    if bounds is None:
        bounds = [-1 * np.inf, np.inf]
    energy_correction_1 = integrator(integrand, left_state, right_state, bounds=bounds)
    return energy_correction_1


def first_order_perturbation_psi(hamiltonian_1, psi_0, E_0, bounds=None, n_upper=10):
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
        temp_array = np.zeros(10000)
        for m in range(0, n_upper):
            if n != m:
                numerator = integrator(integrand, m, n, bounds=bounds)
                denominator = E_0[n] - E_0[m]
                if denominator == 0:
                    print('Opps')
                    return 'infinity'
                # Add together all terms and place into a list
                # psi_function_0 = lambda x, state: psi_0(x, m)
                x = np.linspace(bounds[0], bounds[1], 10000)
                # print(numerator)
                # print(numerator/denominator)
                # print((numerator / denominator) * psi_0(x, m))
                # plt.figure()
                # plt.plot((numerator / denominator) * psi_0(x, m))
                # plt.show()
                temp_array += (numerator / denominator) * psi_0(x, m)
        psi_correction_1[n] = temp_array

    return psi_correction_1


if __name__ == '__main__':
    h_bar = 1
    mass = 1
    energy_list = []
    for i in range(0, 5):
        energy_list.append(i ** 2 * np.pi ** 2 * h_bar ** 2 / (2 * mass * a ** 2))
    print('Energies', energy_list)
    first_order_change_energy = []
    for i in range(0, 5):
        first_order_change_energy.append(first_order_perturbation_energy(h_1, test_psi, [0, a], left_state=i))
    print('First Order Change in Energy', first_order_change_energy)
    psi_correction = first_order_perturbation_psi(h_1, test_psi, energy_list, [0, a], n_upper=5)
    print('First Order Change in Psi', psi_correction)
    x = np.linspace(0, a, 10000)
    '''
    for i in range(1, len(psi_correction)):
        plt.figure()
        plt.title(f'First Order Change in Psi_{i}')
        plt.xlabel(f'x values')
        plt.ylabel(f'Psi1_{i}')
        plt.plot(x, psi_correction[i])
        plt.show()
    '''
    '''
    print('Perturbation in Potential')
    plt.figure()
    plt.plot(x, h_1(x))
    plt.show()
    print('Now adding Psi1 to Psi0')
    '''
    for i in range(1, len(psi_correction)):
        plt.figure(figsize=(10, 5), edgecolor='red', facecolor='lightsteelblue')
        ax1 = plt.subplot(2, 2, 1)
        ax2 = plt.subplot(2, 2, 2)
        ax3 = plt.subplot(2, 2, 3)
        ax1.set_title(f'Psi0[{i}]  + Psi1[{i}]')
        ax2.set_title(f'Psi1[{i}]')
        ax3.set_title(f'Psi0[{i}]')
        ax1.plot(x, test_psi(x, i) + psi_correction[i])
        ax2.plot(x, psi_correction[i])
        ax3.plot(x, test_psi(x, i))
        plt.show()
