import numpy as np

# f(u) = 1 / (1 + e^-u)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# f'(u) = f(u) * (1 - f(u))
def sigmoid_derivative(x):
    return x * (1 - x)

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.1):
        self.lr = learning_rate
        
        # Initialize weights randomly with mean 0
        # W1: (input_size x hidden_size)
        self.W1 = np.random.uniform(size=(input_size, hidden_size))
        # W2: (hidden_size x output_size)
        self.W2 = np.random.uniform(size=(hidden_size, output_size))

    def forward(self, X):
        # Hidden Layer
        self.Z1 = np.dot(X, self.W1)  # Z1 = X * W1
        self.A1 = sigmoid(self.Z1)    # A1 = f(Z1)
        
        # Output Layer
        self.Z2 = np.dot(self.A1, self.W2) # Z2 = A1 * W2
        self.A2 = sigmoid(self.Z2)    # A2 = f(Z2)
        
        return self.A2

    def backward(self, X, Y, A2):
        # A. Calculate Output Layer Error (Delta 2)
        
        # 1. Error: E = Y - A2 (Difference between target and prediction)
        self.E = Y - A2
        
        # 2. Delta 2: Error * Derivative of Output (Chain Rule)
        # Delta_2 = E * f'(Z2)
        # f'(Z2) is calculated using the output A2
        self.Delta2 = self.E * sigmoid_derivative(A2)
        
        # B. Calculate Hidden Layer Error (Delta 1)
        
        # 1. Error Contribution: How much Delta2 should influence the hidden layer
        # Error_Hidden = Delta_2 * W2_T
        self.E_Hidden = np.dot(self.Delta2, self.W2.T)
        
        # 2. Delta 1: Error_Hidden * Derivative of Hidden Activation (Chain Rule)
        # Delta_1 = E_Hidden * f'(A1)
        self.Delta1 = self.E_Hidden * sigmoid_derivative(self.A1)
        
        # C. Calculate Weight Changes (Gradients)
        
        # 1. Weight 2 Gradient: A1_T * Delta_2
        # Transpose A1 needed because X has shape (4, 2) and Delta2 has shape (4, 1)
        self.dW2 = np.dot(self.A1.T, self.Delta2)
        
        # 2. Weight 1 Gradient: X_T * Delta_1
        self.dW1 = np.dot(X.T, self.Delta1)
        
        # D. Update Weights
        self.W2 += self.lr * self.dW2
        self.W1 += self.lr * self.dW1

# --- 3. Training and Execution ---

# Input: 4 training examples, 2 features (XOR problem)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Output: Target (4 examples, 1 output)
Y = np.array([[0], [1], [1], [0]])

# Initialize Network (2 input, 3 hidden, 1 output)
nn = NeuralNetwork(input_size=2, hidden_size=3, output_size=1, learning_rate=0.5)

# Training loop
epochs = 50000
loss_history = []

print(f"Initial Prediction (before training):\n{nn.forward(X).round(3)}\n")

for i in range(epochs):
    # Forward Pass
    A2 = nn.forward(X)
    
    # Calculate Loss (Mean Squared Error)
    loss = np.mean(np.square(Y - A2))
    loss_history.append(loss)
    
    # Backpropagation
    nn.backward(X, Y, A2)

    if i % 10000 == 0:
        print(f"Epoch {i}, Loss: {loss:.6f}")

print(f"\nFinal Prediction (after training):\n{nn.forward(X).round(3)}")

# Plotting the loss
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
plt.plot(loss_history)
plt.title("Training Loss Over Epochs")
plt.xlabel("Epoch")
plt.ylabel("Mean Squared Error (MSE)")
plt.savefig("backpropagation_loss.png")