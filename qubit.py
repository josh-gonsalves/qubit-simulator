import random
import math
import cmath
import numpy as np
from gates import *


"""
    Qubit class representing a single qubit in a quantum system.
    Attributes:
        state: np array representing the qubit state in the computational basis.
        collapsed: boolean indicating if the qubit has been measured.
"""
class Qubit:

    """
        Constructs a Qubit object with state initialized randomly on the Bloch sphere if no state is provided.
        Args:
            state: (Optional) unit-length np array containing the initial qubit state, initialized randomly if none passed.
    """
    def __init__(self, state: np.array = None):
        # theta and phi remain constant; only represent the initial state for debugging
        if state is None:
            self.__theta = math.pi*random.random()
            self.__phi = 2*math.pi*random.random()
            zero_ket = math.cos(self.__theta/2)
            one_ket = cmath.exp(1j * self.__phi) * math.sin(self.__theta/2)
            self.state = np.array([zero_ket, one_ket], dtype=complex)
        else:
            assert np.linalg.norm(state) == 1
            self.state = np.array(state, dtype=complex)
        self.collapsed = False
    
    def __repr__(self):
        return f"Quantum State: {self.state[0]}|0> + ({self.state[1]}|1>)"

    """
        Measures the qubit along some basis, projecting the state onto one of the basis vectors.
        Args:
            basis: measurement basis to project the qubit state onto; dafaults to computational basis.
    """
    def measure(self, basis: np.array = np.eye(2)):
        # check unitary of basis
        assert np.allclose(np.eye(len(basis)), basis @ np.array(basis).T.conj())
        self.collapsed = True

        new_state = basis @ self.get_state()
        new_state = new_state / np.linalg.norm(new_state)

        probs = np.abs(new_state)**2
        outcome = np.random.choice([0, 1], p=probs)
        collapsed_state = basis[outcome]
        self.state = np.array([collapsed_state[0], collapsed_state[1]], dtype=complex)
        return

    def get_state(self):
        return self.state
    
    """
        Applies a quantum gate to the qubit and updates its state.
    """
    def operate(self, g: Gate):
        assert np.allclose(np.eye(len(g)), g*g.T.conj())
        new_state = g*self.get_state()
        self.zero_ket = new_state[0]
        self.one_ket = new_state[1]
        self.state = new_state
        return
    

if __name__ == "__main__":
    tol = 1e-6

    qubit = Qubit(np.array([1,0], dtype=complex))
    print(qubit)
    tot = 0
    gate = PauliX("px")
    gate2 = Hadamard("H")

    for i in range(100):
        qubit = Qubit()
        norm = sum(abs(x)**2 for x in qubit.get_state())
        q_zero = qubit.get_state()[0]
        q_one = qubit.get_state()[1]
        qubit.operate(gate)
        qubit.operate(gate)
        assert (q_zero == qubit.get_state()[0] and q_one == qubit.get_state()[1]), f"{q_zero}, {q_one}, {qubit.get_state()}"
        assert (norm < 1 + tol and norm > 1 - tol), f"{norm}"
        qubit.measure()
        if qubit.get_state()[0] == 1:
            tot += 1
        print(qubit)
    print(tot)
