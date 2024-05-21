import numpy as np
from Approximation import Approximation
from Plotter import Plotter


def main():
    function_type = input(
        "Choose the approximated function: \n"
        "1 - linear (5x - 2)\n"
        "2 - |x|\n"
        "3 - polynomial (x^3 - 2x + 7)\n"
        "4 - trigonometric (sin(x))\n"
        "5 - composite (2 ^ (cos(4x)))\n")
    if function_type not in ["1", "2", "3", "4", "5"]:
        print("Invalid function type selected.")
        return

    approximation_start = float(input("Enter the start of the approximation interval: "))
    approximation_end = float(input("Enter the end of the approximation interval: "))
    approximating_polynomial_degree = int(input("Enter the degree of the approximating polynomial: "))
    epsilon = float(input("Enter the tolerance: "))

    approximation = Approximation(function_type, approximating_polynomial_degree, approximation_start, approximation_end, epsilon)

    x_values = np.linspace(approximation_start, approximation_end, 100)
    original_values = [approximation.function(x) for x in x_values]
    approximated_values = [approximation.ApproximationPolynomial(x) for x in x_values]

    plotter = Plotter()
    plotter.plot_legendre_and_function(approximated_values, original_values, x_values, function_type)

    error = approximation.ApproximationError()
    print("\nApproximation error: ", error)


if __name__ == "__main__":
    main()
