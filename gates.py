import numpy as np

ZERO = np.array((1, 0))
ONE = np.array((0, 1))

class Gate:
    def __init__(self, name, matrix: np.array):
        self.name = name
        self.matrix = matrix

    def __repr__(self):
        return f"Gate(name = {self.name}, matrix = {self.matrix})"
    
    def __len__(self):
        return len(self.matrix)
    
    @property
    def T(self):
        return self.matrix.T
    
    def conj(self): 
        return self.matrix.conj()
    
    def __mul__(self, other):
        return self.matrix @ other

class PauliX(Gate):
    def __init__(self, name):
        print(np.column_stack((ZERO, ONE)))
        super().__init__(name, np.column_stack((ZERO, ONE)))
    
    
    
    
    
