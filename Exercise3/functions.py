import numpy as np


def linear(x):
    return 5 * x - 2


def absolute(x):
    return abs(x)


def horner(x):
    length = 3
    coefficients = [-5, 4, 1]
    result = 0
    for i in range(length - 1, -1, -1):
        result = result * x + coefficients[i]
    return result


def trigonometric(x):
    return 2 * np.sin(4 * x)


def composite(x):
    return abs(np.cos(x) * x)


def function_value(function_type, x):
    functions = {
        "1": linear,
        "2": absolute,
        "3": lambda x: horner(x),
        "4": trigonometric,
        "5": composite
    }
    selected_function = functions.get(function_type)
    if selected_function:
        return selected_function(x)
    else:
        print("Incorrect function type provided.")
