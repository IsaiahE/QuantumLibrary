import numpy as np
from matplotlib import pyplot as plt
import QuantumTools
import array


def variation_principle_energy(required_states):
    # Variational Principle for energy using sines as basis vectors
    # Need to work on dealing with piecewise functions
    a = 2
    a_vector = dict()
    a_vector['1'] = .001
    for i in range(2, required_states + 1):
        # a_vector[f'{i}'] = 1 / np.sqrt(required_states)
        a_vector[f'{i}'] = 0

    def hamiltonian_potential(x):
        return x**2

    def psi_h_psi_integrand(x, n, m):
        product = psi_trial_ground(x, n).conjugate() * hamiltonian_potential(x) * psi_trial_ground(x, m)
        return product

    def basis(x, n):
        return np.sin(n * np.pi * (x + a / 2) / a) * np.sqrt(1 / a)

    def psi_trial_ground(x, number_of_states):
        psi = a_vector['1'] * basis(x, 1)
        if number_of_states != 1:
            for n in range(2, number_of_states + 1):
                psi += a_vector[f'{n}'] * basis(x, n)
        return psi

    def kinetic_energy(number_of_states):
        "h_bar^2 / 2m"
        ke = 0
        for i in range(len(a_vector)):
            ke += a_vector[f'{i + 1}']*np.pi**2*(i+1)**2/(2*a)
        return ke

    def psi_psi(x, n, m):
        product = psi_trial_ground(x, n) * psi_trial_ground(x, m)
        return product

    lowest_energy = 100
    past_lowest_energy = 100
    for a_index in a_vector.keys():
        for i in range(0, 10):
            energy_trial_ground = kinetic_energy(required_states)
            energy_trial_ground += QuantumTools.integrator(psi_h_psi_integrand, required_states, required_states,
                                                          bounds=[-a, a])
            energy_trial_ground = energy_trial_ground / QuantumTools.integrator(psi_psi, required_states, required_states,
                                                                                bounds=[-a, a])
            if lowest_energy > energy_trial_ground:
                past_lowest_energy = lowest_energy
                lowest_energy = energy_trial_ground
                print('a-Vector index:', a_index, 'With Value:', a_vector[a_index])
                print('New Lowest Energy:', lowest_energy)
                if lowest_energy/past_lowest_energy >= .97:
                    print('Convergence Assumed')
                    break

            a_vector[a_index] = a_vector[a_index] + .1
            print(a_vector)


if __name__ == '__main__':
    variation_principle_energy(10)
