import numpy as np

class Gate:
    def __init__(self, name, matrix):
        self.name = name
        self.matrix = matrix

    def __repr__(self):
        return f"Gate(name={self.name}, matrix={self.matrix})"

class       