import numpy as np
import matplotlib.pyplot as plt


class LagrangeInterpolation:
    def __init__(self, nodes, values):
        self.nodes = nodes
        self.values = values

    def interpolate(self, x):
        result = 0
        for i in range(len(self.nodes)):
            term = self.values[i]
            for j in range(len(self.nodes)):
                if i != j:
                    term *= (x - self.nodes[j]) / (self.nodes[i] - self.nodes[j])
            result += term
        return result


class InterpolationPlotter:
    def __init__(self, original_function, interpolation_function, nodes, values):
        self.original_function = original_function
        self.interpolation_function = interpolation_function
        self.nodes = nodes
        self.values = values

    def plot(self):
        x_values = np.linspace(min(self.nodes), max(self.nodes), 1000)
        original_values = self.original_function(x_values)
        interpolation_values = [self.interpolation_function.interpolate(x) for x in x_values]

        plt.plot(x_values, original_values, label="Original Function")
        plt.plot(x_values, interpolation_values, label="Interpolation")
        plt.scatter(self.nodes, self.values, color='red', label="Interpolation Nodes")
        plt.legend()
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Interpolation using Lagrange's method")
        plt.grid(True)
        plt.show()
