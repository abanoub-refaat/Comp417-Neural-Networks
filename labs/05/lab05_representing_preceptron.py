import numpy as np
import matplotlib.pyplot as plt

# normal step activation function & neuron 
def step(x):
    return 1 if x >= 0 else 0


def neuron(x, w, b):
    return step(x @ w + b)

def preceptron(x):
    w = np.array([-1, 2])
    b = 4
    return neuron(x, w, b)

# indentifying random points to be scattered later.
points = np.random.randint(-6, 6, size=(50, 2))

output = np.array([[preceptron(p) for p in points]])

x = np.linspace(-6, 6, 1000)
y= np.linspace(-6, 6, 1000)

X, Y = np.meshgrid(x, y)

X_flat = X.flatten()
Y_flat = Y.flatten()

Z = np.array([[preceptron(p) for p in zip(X_flat, Y_flat)]])
Z = Z.reshape(X.shape)

# plot decision boundary
plt.contour(X, Y, Z, levels=[0], colors=["red"], linewidths=2)
plt.contourf(X, Y, Z, levels=[-0.5, 0.5], colors=["yellow"], alpha=0.5)

plt.scatter(points[:, 0], points[:, 1], c=output, cmap='bwr_r', s=200, edgecolors='k')


plt.title('Neuron decision region: output = 1 highlighted')
margin = 1
plt.xlim(-6 - margin, 6 + margin)
plt.ylim(-6 - margin, 6 + margin)
plt.xlabel('x', loc='left')
plt.ylabel('y', loc='bottom')

# Get current axes
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.show()




