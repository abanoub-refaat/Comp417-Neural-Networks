# preceptron learining algorithm.
import numpy as np

class Preceptron:
    def __init__(self, inputs_size, learing_rate = 0.01):
        self.weights = np.zeros(inputs_size)
        self.bias = 0
        self.learning_rate = learing_rate
    
    @staticmethod
    def step(x):
        return 1 if x >= 0 else 0
    
    def predict(self, x):
        return Preceptron.step(x @ self.weights + self.bias )
    
    def train(self, X, y, epoch = 10):
        for _ in range(epoch):
            for i, x in enumerate(X):
                y_hat = self.predict(x)
                self.weights = self.weights + self.learning_rate * ((y[i] - y_hat) * x)
                self.bias = self.bias + (y[i] - y_hat)

# outside the class
def main():
    X = [[a, b] for a in range(2) for b in range(2)]
    X = np.array(X)
    y_or = [0, 1, 1, 1]
    y_or = np.array(y_or)

    OR_p = Preceptron(2)
    OR_p.train(X, y_or, 1000)

    print(f"weights after training: {OR_p.weights}")
    print(f"bias after training: {OR_p.bias}")

    for x in X:
        print(f"x is: {x}, OR_p: {OR_p.predict(x)}")

if __name__ == "__main__":
    main()