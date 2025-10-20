# single layer preceptron
import numpy as np

def step(x):
    return 1 if x >= 0 else 0

def neuron(x, w, b):
    return step(np.dot(x, w) + b)

def XOR_preceptron1(x):
    n1 = neuron(x, np.array([1, -1]), -1)
    n2 = neuron(x, np.array([-1, 1]), -1)
    n3 = neuron(np.array([n1, n2]), np.array([1, 1]), -1)

    return n3

def XOR_preceptron2(x):
    n1 = neuron(x, np.array([1, 1]), -1)
    n2 = neuron(x, np.array([-1, -1]), 1)
    n3 = neuron(np.array([n1, n2]), np.array([1, 1]), -2)

    return n3

def more_generic_model(x):
    n1 = neuron(x[[0, 1]], np.array([1, 1]), -2)
    n2 = neuron(x[[0, 2]], np.array([1, 1]), -2)
    n3 = neuron(x[[1, 3]], np.array([-1, 1]), -1)
    n4 = neuron(x[[0, 2, 3]], np.array([-1, 1, 1]), -2)

    n5 = neuron(np.array([n1, n2]), np.array([1, -1]), 0)
    n6 = neuron(np.array([n3, n4]), np.array([1, 1]), -1)

    n7 = neuron(np.array([n5, n6]), np.array([1, 1]), -2)

    return n7

def boolean_fun(x):
    return int(((x[3] and not x[0] and x[3]) or ( x[3] and not x[1])) and ((x[0] and x[1]) or not(x[0] and x[2])))

X = np.array([[a, b] for a in range(2) for b in range(2)])
X = np.array(X)

for x in X:
    print(f"XOR_preceptron1(x) is {XOR_preceptron1(x)}, XOR{x} = {x[0] ^ x[1]}")

print("\nbreak\n")

for x in X:
    print(f"XOR_preceptron2(x) is {XOR_preceptron2(x)}, XOR{x} = {x[0] ^ x[1]}")


print("\nbreak\n")

X = [[a, b, c, d] for a in range(2) for b in range(2) for c in range(2) for d in range(2)]
X = np.array(X)
for x in X:
    print(f"BF_MLP = {more_generic_model(x)}, BF{x} = {boolean_fun(x)}")