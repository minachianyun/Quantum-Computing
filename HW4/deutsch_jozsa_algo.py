from qiskit import QuantumCircuit, Aer, execute

# 定義Deutsch-Jozsa oracle
def dj_problem_oracle(problem):
    """Returns a 5-qubit Deutsch-Joza Oracle"""
    qc = QuantumCircuit(5)  # 創建量子電路，5個量子位元
    if problem == 1:
        for q in range(4):
            qc.cx(q, 4)  # 奇數個量子位元取XOR，最後一位量子位元存儲結果
    elif problem == 2:
        qc.cx(0, 4)  # 前兩個量子位元對第5個量子位元應用CNOT門，最後一位量子位元存儲結果
        qc.cx(1, 4)
    elif problem == 3:
        qc.cx(2,4)  # 第三個量子位元對第5個量子位元應用CNOT門，最後一位量子位元存儲結果
    else:
        print("There are only currently 3 oracles in this problem set, returning empty (balanced) gate")
    return qc.to_gate()


def dj_algorithm(oracle):
    # 創建一個具有5個量子位和4個經典位的QuantumCircuit對象，並將其分配給變量dj_circuit
    dj_circuit = QuantumCircuit(5, 4)
    # 在第5個量子位元上使用X閘
    dj_circuit.x(4)
    # 對於每個量子位元使用H閘
    for i in range(5):
        dj_circuit.h(i)
    # 將oracle代表的量子電路附加到dj_circuit上，使用range(5)設置量子電路中的所有量子位元
    dj_circuit.append(oracle, range(5))
    # 對前4個量子位應用H閘
    for i in range(4):
        dj_circuit.h(i)
    # 將前4個量子位元量測到相應的古典位元上
    for i in range(4):
        dj_circuit.measure(i, i)
    # 返回dj_circuit量子電路對象作為函數dj_algorithm的結果
    return dj_circuit
# 測資的個數
n = int(input())
for _ in range(n):
    problem = int(input())
    oracle_gate = dj_problem_oracle(problem)
    circuit = dj_algorithm(oracle_gate)
    simulator = Aer.get_backend('aer_simulator')
    counts = execute(circuit, backend=simulator).result().get_counts()
    print(max(counts, key=counts.get))