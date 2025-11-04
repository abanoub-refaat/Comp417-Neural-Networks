import matplotlib.pyplot as plt
import numpy as np

def line_from_two_points(p1, p2):
    # check for undifined slope
    if p1[0] == p2[0]:
        return None, p1[0]
    # m = (y2 - y1)/ (x2 - x1)
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])

    # b = y - mx
    b = p1[1] - m * p1[0]
    return m, b

# return an array [A, B, C] where Ax + By + C = 0
def line_form(p1, p2, above=True):
    m, b = line_from_two_points(p1, p2)
    if m is None:
        # x = b (vertical line)
        return [-1, 0, b] if above else [1, 0, b]
    
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
    l1 = line_form((1, 0), (0, 1), above=False)
    l2 = line_form((0, -1), (-1, 0), above=True)
    l3 = line_form((-1, 0), (0, 1), above=False)
    l4 = line_form((0, -1), (1, 0), above=True)

    # this is a square shape we have 4 lines -> 4 neuron and the and neuron is the final one we will return
    n1 = neuron(x, l1[:2], l1[2])
    n2 = neuron(x, l2[:2], l2[2])
    n3 = neuron(x, l3[:2], l3[2])
    n4 = neuron(x, l4[:2], l4[2])
    n5 = neuron(np.array([n1, n2, n3, n4]), np.array([1, 1, 1, 1]), -4)
    return n5

# Drawing this shape using `matplotlib`
points = np.random.randint(-6, 6, size=(50, 2))
outputs = np.array([[preceptron(p) for p in points]])
limit = 6

x = np.linspace(- limit, limit, 1000)
y = np.linspace( - limit, limit, 1000)

X, Y = np.meshgrid(x, y)
Z = np.array([[preceptron((xx, yy)) for xx, yy in zip(row_x, row_y)] for row_x, row_y in zip(X, Y)])

plt.figure(figsize=(32, 15))
plt.title("Desision Region formed by multiple neurons")

plt.contour(X, Y, Z, levels=[0], colors=["blue"], linewidth=2)
plt.contourf(X, Y, Z, levels=[-0.5, 0.5], colors=["yellow"], alpha=0.5)

plt.scatter(points[:, 0], points[:, 1], c=outputs, cmap="bwr_r", s=20, edgecolors="k")

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

plt.show()
