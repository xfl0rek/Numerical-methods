from scipy.integrate import quad
import Functions as f


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

    result, error = quad(f.function_value(function_type), start_interval, end_interval)
    print(result)
    print(error)


if __name__ == "__main__":
    main()
