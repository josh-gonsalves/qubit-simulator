import random
import math
import cmath
import numpy as np
from gates import Gate, PauliX

class Qubit:

    def __init__(self):
        self.theta = math.pi*random.random()
        self.phi = 2*math.pi*random.random()
        self.zero_ket = math.cos(self.theta/2)
        self.one_ket = cmath.exp(1j * self.phi) * math.sin(self.theta/2)
    
    def __repr__(self):
        return f"Quantum State: {self.zero_ket}|0> + ({self.one_ket}|1>)"

    def measure_std(self):
        if random.random() < abs(self.zero_ket)**2:
            return 0
        return 1

    def get_state(self):
        return np.array([self.zero_ket, self.one_ket], dtype=complex)
    
    def operate(self, g: Gate):
        assert np.allclose(np.eye(len(g)), g*g.T.conj())
        new_state = g*self.get_state()
        self.zero_ket = new_state[0]
        self.one_ket = new_state[1]
    

if __name__ == "__main__":
    tol = 1e-6

    qubit = Qubit()
    print(qubit)
    tot = 0
    gate = PauliX("px")

    for i in range(100):
        qubit = Qubit()
        norm = sum(abs(x)**2 for x in qubit.get_state())
        q_zero = qubit.get_state()[0]
        q_one = qubit.get_state()[1]
        assert (norm < 1 + tol and norm > 1 - tol), f"{norm}"
        if qubit.measure_std() == 1:
            tot += 1
        
        qubit.operate(gate)
        assert (q_zero == qubit.zero_ket and q_one == qubit.one_ket)


    print(tot)
