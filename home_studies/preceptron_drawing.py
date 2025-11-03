import numpy as np
import matplotlib.pyplot as plt

def step(x):
    return 1 if x >= 0 else 0

def neuron(x, w, b):
    return step(np.dot(x, w) + b)

def perceptron(x):
    w = np.array([-1, 2])
    b = 4
    n1 = neuron(x, w, b)
    return n1

points = np.random.randint(-6, 6, size=(50, 2))

outputs = np.array([[perceptron(p) for p in points]])

limitPoint = 6

x = np.linspace(-limitPoint, limitPoint, 200)
y = np.linspace(-limitPoint, limitPoint, 200)
X, Y = np.meshgrid(x, y)
Xf = X.flatten()
Yf = Y.flatten()

Z = np.array([[perceptron(p) for p in zip(Xf, Yf)]])
Z = Z.reshape(X.shape)

# Plot decision boundary
plt.contour(X, Y, Z, levels=[0], colors=['blue'], linewidths=2)

# Highlight region where neuron output == 1
plt.contourf(X, Y, Z, levels=[-0.5, 0.5], colors=['yellow'], alpha=0.5)

# Optionally scatter sample points
plt.scatter(points[:, 0], points[:, 1], c=outputs, cmap='bwr_r', s=200, edgecolors='k')

plt.title('Neuron decision region: output = 1 highlighted')
margin = 1
plt.xlim(-limitPoint - margin, limitPoint + margin)
plt.ylim(-limitPoint - margin, limitPoint + margin)
plt.xlabel('x', loc='left')
plt.ylabel('y', loc='bottom')

# Get current axes
ax = plt.gca()
# Move left and bottom spines (axes lines) to the center
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.show()
