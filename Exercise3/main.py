import functions as f


def main():
    function_type = input("Enter function type (1: linear, 2: absolute, 3: horner, 4: trigonometric, 5: composite): ")
    x = float(input("Enter the value of x: "))

    result = f.function_value(function_type, x)
    if result is not None:
        print("Result:", result)


if __name__ == "__main__":
    main()
