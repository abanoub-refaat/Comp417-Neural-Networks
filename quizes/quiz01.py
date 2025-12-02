import matplotlib.pyplot as plt
import numpy as np

def line_from_two_points(p1, p2):
    # check for undifined slope
    if p1[0] == p2[0]:
        return None, p1[0]
    # m = (y2 - y1)/ (x2 - x1)
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])

    # b = y - mx (y-intercept)
    b = p1[1] - m * p1[0]
    return m, b

# return an array [A, B, C] where Ax + By + C = 0
def line_form(p1, p2, above=True):
    m, b = line_from_two_points(p1, p2)
    
    # vertical line logic
    if m is None:
        # Vertical line x = b (b is the x-intercept)
        # above=True means to the right (x >= b) -> x - b >= 0 -> [1, 0, -b]
        # above=False means to the left (x <= b) -> -x + b >= 0 -> [-1, 0, b]
        return [1, 0, -b] if above else [-1, 0, b]

    # Sloped line logic (Horizontal lines are handled here as m=0)
    if above:
        A, B, C = -m, 1, -b
    else:
        A, B, C = m, -1, b

    return [A, B, C]

# Redifining the step, neuron, and preceptron functions to test the lines
def step(x):
    return 1 if x >= 0 else 0

def neuron(x, w, b):
    return step(np.dot(x, w) + b)

def preceptron(x):
    # fist triangle (t1)
    l1 = line_form((-2, 7), (2, 7), above=False) 
    l2 = line_form((-2, 7), (0, 5), above=True)
    l3 = line_form((2, 7), (0, 5), above=True)

    n1 = neuron(x, l1[:2], l1[2])
    n2 = neuron(x, l2[:2], l2[2])
    n3 = neuron(x, l3[:2], l3[2])

    # AND gate for t1: requires all 3 inputs to be 1
    n_t1 = neuron(np.array([n1, n2, n3]), np.array([1, 1, 1]), -3)

    # rectangle (rec)
    l4 = line_form((-3, 3), (3, 3), above=False) 
    l5 = line_form((-3, 3), (-3, -5), above=True) 
    l6 = line_form((3, 3), (3, -5), above=False) 
    l7 = line_form((-3, -5), (3, -5), above=True) 

    n4 = neuron(x, l4[:2], l4[2])
    n5 = neuron(x, l5[:2], l5[2])
    n6 = neuron(x, l6[:2], l6[2])
    n7 = neuron(x, l7[:2], l7[2])

    # AND gate for rec: requires all 4 inputs to be 1
    n_rec = neuron(np.array([n4, n5, n6, n7]), np.array([1, 1, 1, 1]), -4)

    # second triangle (t2)
    # NOTE: Lines l8, l9, l10 are collinear (all lie on y=x), 
    # so the AND gate n_t2 will only activate on the line segment itself.
    l8 = line_form((0, 0), (2, 2), above=True)
    l9 = line_form((-2, -2), (-0, 0), above=False)
    l10 = line_form((-2, -2), (2, 2), above=False)

    n8 = neuron(x, l8[:2], l8[2])
    n9 = neuron(x, l9[:2], l9[2])
    n10 = neuron(x, l10[:2], l10[2])

    # AND gate for t2: requires all 3 inputs to be 1
    n_t2 = neuron(np.array([n8, n9, n10]), np.array([1, 1, 1]), -3)

    # OR gate between rec and t2: n_rec OR n_t2
    # OR gate: requires at least 1 input to be 1 (weight 1, threshold 1-epsilon = -1)
    n_t_r = neuron(np.array([n_rec, n_t2]), np.array([1, 1]), -1) # Corrected threshold from -2 to -1 for OR

    # AND gate for final output: n_t1 AND n_t_r
    # AND gate: requires both 2 inputs to be 1 (weight 1, threshold 2-epsilon = -2)
    n_output = neuron(np.array([n_t1, n_t_r]), np.array([1, 1]), -2) # Corrected threshold from -1 to -2 for AND

    # return the final output
    return n_output

# Drawing this shape using `matplotlib`
points = np.random.randint(-10, 10, size=(50, 2))
outputs = np.array([[preceptron(p) for p in points]])
limit = 10

x = np.linspace(- limit, limit, 1000)
y = np.linspace( - limit, limit, 1000)

X, Y = np.meshgrid(x, y)
X_flat = X.flatten()
Y_flat = Y.flatten()

Z = np.array([[preceptron(p) for p in zip(X_flat, Y_flat)]])
Z = Z.reshape(X.shape)

plt.figure(figsize=(10, 10)) # Reduced figure size for better display
plt.title("Decision Region formed by multiple neurons (T1 AND (REC OR T2))")

plt.contour(X, Y, Z, levels=[0], colors=["blue"], linewidths=2)
plt.contourf(X, Y, Z, levels=[-0.5, 0.5], colors=["yellow"], alpha=0.5)

plt.scatter(points[:, 0], points[:, 1], c=outputs.flatten(), cmap="bwr_r", s=50, edgecolors="k")

# Labeling and axis styling
plt.xlabel("x", loc="right")
plt.ylabel("y", loc="top")
plt.xlim(-limit, limit)
plt.ylim(-limit, limit)
plt.grid(alpha=0.3)

# Center axes
ax = plt.gca()
ax.spines["left"].set_position("center")
ax.spines["bottom"].set_position("center")
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")

plt.savefig("decision_region.png")