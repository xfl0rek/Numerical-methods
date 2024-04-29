import numpy as np


def linear(x):
    return 5 * x - 2


def absolute(x):
    return abs(x)


def polynomial(x):
    length = 4
    coefficients = [1, 0, -2, 7]
    result = coefficients[0]
    for i in range(1, length):
        result = result * x + coefficients[i]
    return result


def trigonometric(x):
    return 2 * np.sin(4 * x)


def composite(x):
    return 2 ** (np.cos(4 * x))


def function_value(function_type):
    functions = {
        "1": linear,
        "2": absolute,
        "3": polynomial,
        "4": trigonometric,
        "5": composite
    }
    return functions.get(function_type)
