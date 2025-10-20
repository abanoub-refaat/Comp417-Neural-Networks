import numpy as np

def step(x):
    return 1 if x >= 0 else 0

def neuron(x, w, b):
    return step(np.dot(x, w) + b)

def nor_p(x):
    n = x.shape[0]
    return neuron(x, np.array(np.ones(n) * -1), 0)

print("--- N=3 Generalized NOR Perceptron Test ---")
x_inputs = np.array([[a, b, c] for a in range(2) for b in range(2) for c in range(2)])

for x in x_inputs:
    print(f"NOR({x}): output = {nor_p(x)}, correct = {1 if np.sum(x) == 0 else 0}")
