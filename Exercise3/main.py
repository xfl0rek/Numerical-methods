import Functions as f
import LagrangeInterpolation
import InterpolationPlotter


def main():
    function_type = input(
        "Choose the interpolated function (1 - linear, 2 - |x|, 3 - polynomial, 4 - trigonometric, 5 - composite): ")
    if function_type not in ["1", "2", "3", "4", "5"]:
        print("Invalid function type selected.")
        return

    start_interval = float(input("Enter the start of the interpolation interval: "))
    end_interval = float(input("Enter the end of the interpolation interval: "))

    num_nodes = int(input("Enter the number of interpolation nodes: "))

    nodes = [start_interval + (end_interval - start_interval) * i / (num_nodes - 1) for i in range(num_nodes)]
    values = [f.function_value(function_type)(node) for node in nodes]

    interpolation_function = f.function_value(function_type)

    lagrange_interpolation = LagrangeInterpolation.LagrangeInterpolation(nodes, values, interpolation_function)

    plotter = InterpolationPlotter.InterpolationPlotter(interpolation_function, lagrange_interpolation, nodes, values)
    plotter.plot()


if __name__ == "__main__":
    main()
