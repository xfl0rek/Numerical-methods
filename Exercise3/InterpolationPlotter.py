import matplotlib.pyplot as plt
import numpy as np


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
