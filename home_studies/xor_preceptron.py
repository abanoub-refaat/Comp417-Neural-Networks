import numpy as np

def step(x):
    return 1 if x >= 0 else 0

def neuron(x, w, b):
    return step(np.dot(x, w) + b)

def xor_p(x):
    n1 = neuron(x, np.array([1, 1]), -1)
    n2 = neuron(x, np.array([-1, -1]), 1)
    n3 = neuron(np.array([n1, n2]), np.array([1, 1]), -2)

    return n3


print("--- N=2 XOR Perceptron Test ---")
x_inputs = np.array([[a, b] for a in range(2) for b in range(2)])

for x in x_inputs:
    print(f"NOR({x}): output = {xor_p(x)}, correct = {x[0] ^ x[1]}")