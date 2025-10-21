import numpy as np

def step(x):
    return 1 if x >= 0 else 0

def neuron(x, w, b):
    return step(np.dot(x, w) + b)

# O = y'z' + w'xy' + x'z'
def simplified_bool_1(x):
    return int((not x[2] and not x[3]) or (not x[0] and x[1] and not x[2]) or not x[1] and not x[3])

# mulitlayer preceptron for O function
def multi_p(x):
    n1 = neuron(x[[2, 3]], np.array([-1, -1]), 0)
    n2 = neuron(x[[0, 1, 2]], np.array([-1, 1, -1]), -1)
    n3 = neuron(x[[1, 3]], np.array([-1, -1]), 0)

    return neuron(np.array([n1, n2, n3]), np.array([1, 1, 1]), -1)

def xor_p(x):
    n1 = neuron(x, np.array([1, 1]), -1)
    n2 = neuron(x, np.array([-1, -1]), 1)
    n3 = neuron(np.array([n1, n2]), np.array([1, 1]), -2)

    return n3

def multi_xor_p(x_inputs):
    n = xor_p(x_inputs[[0, 1]])
    for x in range(2,x_inputs.shape[0] ):
       n = xor_p(np.array([n, x_inputs[x]]))
    return n

def text_multi_xor_p(x_inputs):
    n = x_inputs[0] ^ x_inputs[1]
    for x in range(2,x_inputs.shape[0] ):
       n = n ^ x_inputs[x]
    return n

# test for multilayer preceptron
def main():
    x_inputs = np.array([[a, b, c, d] for a in range(2) for b in range(2) for c in range(2) for d in range(2)])

    print("----- test simplified boolean function ------")

    for x in x_inputs:
        print(f"x{x} is: {multi_p(x)}, correct: {simplified_bool_1(x)}")

    print("\n------- test generic multi_xor function -----")

    for x in x_inputs:
        print(f"x{x} is: {multi_xor_p(x)} correct: {text_multi_xor_p(x)}")

if __name__ == "__main__":
    main()