import numpy as np
import matplotlib.pyplot as plt


def plot_function(func, a, b, f_type):
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

    x = np.linspace(a, b, 1000)
    y = func(x)
    plt.plot(x, y, label="Function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()
