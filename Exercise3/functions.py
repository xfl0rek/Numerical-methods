import math


def linear(x):
    return 5 * x - 2


def absolute(x):
    return abs(x)


def horner(coefficients, x, length):
    result = 0
    for i in range(length - 1, -1, -1):
        result = result * x + coefficients[i]
    return result


def trigonometric(x):
    return 2 * math.sin(4 * x)


def composite(x):
    return abs(math.cos(x) * x)


def function_value(type, x):
    if type == "1":
        return linear(x)
    elif type == "2":
        return absolute(x)
    elif type == "3":
        return horner([-5, 4, 1], x, 3)
    elif type == "4":
        return trigonometric(x)
    elif type == "5":
        return composite(x)
    else:
        print("Incorrect function type provided.")
