from gates import *
from qubit import Qubit


# FIX: Use a dataclass that allows for the saving of order of qubits in circuit

class CircuitQubit:
    def __init__(self, element: Qubit, order: int = 0):
        self.element = element
        self.order = order

class Circuit: 

    def __init__(self, qubits: dict[Qubit : [Gate]] = {}, gates: dict[Gate : int] = {}, mapping: dict[Gate : [Qubit]] = {}):
        self.qubits = qubits
        self.gates = gates
        self.mapping = mapping
        self.max_depth = 0
        return

    def add_qubit(self, qubit: Qubit):
        self.qubits[qubit] = []
        return
    
    def add_qubits(self, qubits: list[Qubit]):
        for qubit in qubits:
            self.add_qubit(qubit)
        return
    
    def add_gate(self, gate: Gate, qubits: list[Qubit] = None):
        assert gate not in self.gates, "Gate {gate} already in circuit"
        for qubit in qubits:
            assert qubit in self.qubits, "Qubit {qubit} not in circuit"
            self.qubits[qubit].append(gate)
            self.max_depth = max(self.max_depth, len(self.qubits[qubit]))
        self.gates[gate] = len(self.gates)
        if qubits is not None:
            self.mapping[gate] = qubits
        return
    
    def add_gates(self, gates: dict[Gate : list[Qubit]]):
        for gate in gates:
            self.add_gate(gate, gates[gate])

    def map(self, gate: Gate, qubits: list[Qubit]):
        assert gate in self.gates, "Gate {gate} not in circuit"
        for qubit in qubits:
            assert qubit in self.qubits, "Qubit {qubit} not in circuit"
            self.max_depth = max(self.max_depth, len(self.qubits[qubit]))
        self.mapping[gate] = qubits
        return
    
    def generate_circuit(self):
        circuit = np.zeros((len(self.qubits), self.max_depth), dtype=Gate)
        for qubit in self.qubits:
            for gate in self.qubits[qubit]:
                pass
        # FIX THIS