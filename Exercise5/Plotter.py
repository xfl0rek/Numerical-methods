from matplotlib import pyplot as plt


class Plotter:
    @staticmethod
    def plot_legendre_and_function(legendre_values, function_values, x_values, f_type):
        if f_type == '1':
            plt.title("5x - 2")
        elif f_type == '2':
            plt.title("|x|")
        elif f_type == '3':
            plt.title("x^3 - 2x + 7")
        elif f_type == "4":
            plt.title("2sin(4x)")
        elif f_type == "5":
            plt.title("2 ^ (cos(4x))")

        plt.plot(x_values, legendre_values, label='Legendre Polynomial')
        plt.plot(x_values, function_values, label='Original Function')
        plt.xlabel("x")
        plt.ylabel("Value")
        plt.legend()
        plt.grid(True)
        plt.show()
