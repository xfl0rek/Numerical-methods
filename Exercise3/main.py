import functions as f
import LagrangeInterpolation


def main():
    function_type = input("Enter function type (1: linear, 2: absolute, 3: horner, 4: trigonometric, 5: composite): ")
    x = float(input("Enter the value of x: "))

    result = f.function_value(function_type, x)
    if result is not None:
        print("Result:", result)


if __name__ == "__main__":
    nodes = [1, 2, 3, 4]
    values = [1, 4, 9, 16]
    lagrange_interpolation = LagrangeInterpolation.LagrangeInterpolation(nodes, values)
    plotter = LagrangeInterpolation.InterpolationPlotter(f.composite, lagrange_interpolation, nodes, values)
    plotter.plot()

    main()
