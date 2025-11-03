import numpy as np
import random

class Perceptron:
    def __init__(self, input_size, epoch=10, learning_rate=0.01):
        self.weights = np.zeros(input_size)
        self.bias = 0

        self.epochs = epoch
        self.learning_rate = learning_rate

    def random_init(self, input_size):
        self.weights = np.random.rand(input_size)
        self.bias = random.random()
    
    @staticmethod
    def step(x):
        return 1 if x >= 0 else 0
    
    def predict(self, x):
        return Perceptron.step(x @ self.weights + self.bias)
    
    def train(self, X, y):
        for _ in range(self.epochs):
            for i, x in enumerate(X):
                y_hat = self.predict(x)
                self.weights = self.weights + self.learning_rate * (y[i] - y_hat) * x
                self.bias = self.bias + self.learning_rate * (y[i] - y_hat)
            if (y == y_hat).all():
                break
