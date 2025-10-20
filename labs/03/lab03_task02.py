import numpy as np

"""
Activation step function
"""
def step(x):
    return 1 if x >= 0 else 0

"""
Generic neural
X: inputs vector
W: weights vector
b: bias
"""
def neuron(X, W, b):
    return step(np.dot(X, W) + b)

# task 01
# implement a generic and preceptron that accepts n inputs

def and_p(X):
    # n is the number of inputs
    n = X.shape[0] 
    return neuron(X, np.ones(n), -n)

# test the genric and preceptron
print("--- N=3 Generalized AND Perceptron Test ---")

x_inputs = np.array([[a, b, c] for a in range(2) for b in range(2) for c in range(2)])

for x in x_inputs:
    print(f"AND({x}): Output = {and_p(x)}, Correct = {1 if np.sum(x) == 3 else 0}")

print("\n--- N=5 Generalized AND Perceptron Test ---")

x_inputs = np.array([[a, b, c, d, e] for a in range(2) for b in range(2) for c in range(2) for d in range(2) for e in range(2)])

for x in x_inputs:
    print(f"AND({x}): Output = {and_p(x)}, Correct = {1 if np.sum(x) == 5 else 0}")

# task 02
# Implement a genric or preceptron

def or_p(X):
    n = X.shape[0]
    return neuron(X, np.ones(n), -1)

print("\n--- N=5 Generalized OR Perceptron Test ---")

x_inputs = np.array([[a, b, c, d, e] for a in range(2) for b in range(2) for c in range(2) for d in range(2) for e in range(2)])

for x in x_inputs:
    print(f"AND({x}): Output = {or_p(x)}, Correct = {1 if np.sum(x) >= 1 else 0}")