from qiskit import QuantumCircuit, Aer, QuantumRegister, ClassicalRegister
from qiskit.visualization import array_to_latex
import numpy as np

v = QuantumRegister(2,'v')
cr = ClassicalRegister(2,'cbits')
qc = QuantumCircuit(v,cr)
qc.x(1)
qc.h([0,1])
qc.cx(0,1)
sim = Aer.get_backend('aer_simulator')
qc.save_unitary()
unitary = sim.run(qc).result().get_unitary()
print([['{:.2f}'.format(item) for item in sublist] for sublist in np.array(unitary)])