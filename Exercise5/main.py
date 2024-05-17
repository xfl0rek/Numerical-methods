import numpy as np
from matplotlib import pyplot as plt

from Functions import function_value
from LegendreApproximation import LegendreApproximation


def main():
    function_type = input(
        "Choose the approximated function: \n"
        "1 - linear (5x - 2)\n "
        "2 - |x|\n "
        "3 - polynomial (x^3 - 2x + 7)\n "
        "4 - trigonometric (2sin(4x))\n "
        "5 - composite (2 ^ (cos(4x)))\n")
    if function_type not in ["1", "2", "3", "4", "5"]:
        print("Invalid function type selected.")
        return

    approximation_start = float(input("Enter the start of the approximation interval: "))
    approximation_end = float(input("Enter the end of the interpolation interval: "))
    approximating_polynomial_degree = int(input("Enter the degree of the approximating polynomial: "))
    epsilon = float(input("Enter the tolerance: "))

    selected_function = function_value(function_type)
    if selected_function is None:
        print("Invalid function type selected.")
        return

    legendre = LegendreApproximation(approximating_polynomial_degree)
    x_values = np.linspace(approximation_start, approximation_end, 1000)
    legendre_values = [legendre.function_value(x) for x in x_values]

    plt.plot(x_values, legendre_values)
    plt.title("Legendre Polynomial")
    plt.xlabel("x")
    plt.ylabel("Legendre Polynomial Value")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
