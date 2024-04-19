import Functions as f
import LagrangeInterpolation
import LoadData
import InterpolationPlotter


def main():
    function_type = input("Choose the interpolated function (1 - linear, 2 - |x|, 3 - polynomial, 4 - trigonometric, 5 - composite): ")
    if function_type not in ["1", "2", "3", "4", "5"]:
        print("Invalid function type selected.")
        return

    filename = input("Enter the filename with data: ")

    try:
        nodes, values = LoadData.load_data(filename)
    except FileNotFoundError:
        print("File not found.")
        return

    if function_type == "3":
        interpolation_function = f.horner
    else:
        interpolation_function = f.function_value(function_type)

    if interpolation_function is None:
        print("Invalid function type.")
        return

    lagrange_interpolation = LagrangeInterpolation.LagrangeInterpolation(nodes, values)
    plotter = InterpolationPlotter.InterpolationPlotter(interpolation_function, lagrange_interpolation, nodes, values)
    plotter.plot()


if __name__ == "__main__":
    main()
