from matplotlib import pyplot as plt


class Plotter:
    @staticmethod
    def plot_legendre_and_function(legendre_values, function_values, x_values):
        plt.plot(x_values, legendre_values, label='Legendre Polynomial')
        plt.plot(x_values, function_values, label='Original Function')
        plt.title("Approximation and Original Function")
        plt.xlabel("x")
        plt.ylabel("Value")
        plt.legend()
        plt.grid(True)
        plt.show()
