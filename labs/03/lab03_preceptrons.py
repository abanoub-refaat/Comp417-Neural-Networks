# single layer preceptron
import numpy as np

#############################################################

# activation (step) function definition 
def step(x):
    return 1 if x >= 0 else 0

# generic neural
def neuron(x, w, b):
    return step(np.dot(x, w) + b)

# AND preceptron
def AND_preceptron(x):
    return neuron(x, np.array([1,1]),-2)

def OR_preceptron(x):
    return neuron(x, np.array([1, 1]), -1)

def BF_MLP(x):
    n1 = neuron(x[:2], np.array([1, -1]), -1)
    n2 = neuron(x, np.array([-1,1,1]), -2)
    n3 = neuron(x, np.array([1,-1,-1]), 1)

    n4 = neuron(np.array([n1, n2, n3]), np.array([-1,1,1]), 0)
    return n4

def boolean_fun(x):
    return bool(not(x[0] and not x[1]) or (not x[0] and x[1] and x[2]) or (x[0] or not x[1] or not x[2]))

#############################################################

# test AND preceptron
X = np.array([[a, b] for a in range(2) for b in range(2)])

for x in X:
    print(f"AND_preceptron(x) is {AND_preceptron(x)}, AND{x} = {x[0] and x[1]}")

# test OR preceptron

for x in X:
    print(f"OR_preceptron(x) is {OR_preceptron(x)}, OR{x} = {x[0] or x[1]}")


# test multilayer preceptron
X = [[a, b, c] for a in range(2) for b in range(2) for c in range(2)]

for x in X:
    print(f"BF_MLP = {BF_MLP(x)}, BF{x} = {boolean_fun(x)}")
