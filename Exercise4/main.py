from Functions import function_value
from CompositeNewtonCotes import CompositeNewtonCotes
from LegendreQuadrature import LegendreQuadrature


def main():
    function_type = input(
        "Choose the interpolated function: \n"
        "1 - linear (5x - 2)\n "
        "2 - |x|\n "
        "3 - polynomial (x^3 - 2x + 7)\n "
        "4 - trigonometric (2sin(4x))\n "
        "5 - composite (2 ^ (cos(4x)))\n")
    if function_type not in ["1", "2", "3", "4", "5"]:
        print("Invalid function type selected.")
        return

    start_interval = float(input("Enter the start of the interpolation interval: "))
    end_interval = float(input("Enter the end of the interpolation interval: "))
    tolerance = float(input("Enter the tolerance for the integration: "))

    selected_function = function_value(function_type)
    if selected_function is None:
        print("Invalid function type selected.")
        return

    integrator = CompositeNewtonCotes(selected_function)
    integrator2 = LegendreQuadrature(selected_function)
    result = integrator.integrate(start_interval, end_interval, 1, tolerance)
    result2 = integrator2.integrate(start_interval, end_interval)
    print("Result of composite Newton Cotes: ", result)
    print("Result of Legendre quadrature: ", result2)


if __name__ == "__main__":
    main()
