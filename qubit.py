import random
import math

class Qubit:

    def __init__(self):
        self.theta = math.pi*random.random()
        self.phi = 2*math.pi*random.random()
        self.zero_ket = math.cos(self.theta/2)
        self.one_ket = math.sin(self.theta/2)
        self.rel_phase = math.e**self.phi # e^(i*phi)
    
    def __repr__(self):
        if self.one_ket < 0:
            return f"Quantum State: {self.zero_ket}|0> + ({self.one_ket}|1>)"
        return f"Quantum State: {self.zero_ket}|0> + {self.one_ket}|1>"

    def measure_std(self):
        val = random.random()
        if val < self.zero_ket**2:
            return 0
        else: return 1

    def get_state(self):
        return (self.zero_ket, self.one_ket)
    

if __name__ == "__main__":
    tol = 1e-6

    qubit = Qubit()
    print(qubit)
    tot = 0

    for i in range(100):
        qubit = Qubit()
        norm = sum(x**2 for x in qubit.get_state())
        assert (norm < 1 + tol and norm > 1 - tol), f"{norm}"
        if qubit.measure_std() == 1:
            tot += 1

    print(tot)
