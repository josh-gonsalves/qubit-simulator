import numpy as np

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
        super().__init__(name, np.array([[0, 1], [1, 0]]))
    
class PauliY(Gate):
    def __init__(self, name):
        super().__init__(name, np.array([[0, -1j], [1j, 0]]))

class PauliZ(Gate):
    def __init__(self, name):
        super().__init__(name, np.array([[1, 0], [0, -1]]))

class Hadamard(Gate):
    def __init__(self, name):
        super().__init__(name, (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]]))


    
    
    
    
