import Functions as f
import LagrangeInterpolation
import LoadData


def main():
    return None


if __name__ == "__main__":
    nodes, values = LoadData.load_data("DataFiles/data1.txt")
    lagrange_interpolation = LagrangeInterpolation.LagrangeInterpolation(nodes, values)
    plotter = LagrangeInterpolation.InterpolationPlotter(f.composite, lagrange_interpolation, nodes, values)
    plotter.plot()

    main()
