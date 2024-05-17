import numpy as np

from Functions import function_value
from LegendreApproximation import LegendreApproximation
from Plotter import Plotter


def calculate_approximation_error(original_values, approximated_values):
    errors = [abs(orig - approx) for orig, approx in zip(original_values, approximated_values)]
    max_error = max(errors)
    mean_error = sum(errors) / len(errors)
    return max_error, mean_error


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
    function_values = [selected_function(x) for x in x_values]

    max_err, mean_err = calculate_approximation_error(function_values, legendre_values)
    print(f"Max approximation error: {max_err}")
    print(f"Mean approximation error: {mean_err}")

    Plotter.plot_legendre_and_function(legendre_values, function_values, x_values)


if __name__ == "__main__":
    main()
