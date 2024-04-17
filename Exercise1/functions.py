import horner
import numpy as np
from decimal import Decimal as d
import math


def polynomial(arg):
    value = horner.horner([-5, 4, 1], arg, 3)
    return d(value)


def trigonometric(arg):
    return d(2 * math.sin(4 * arg))


def exponential(arg):
    return d(2 ** arg - 2)


def composite_function(arg):
    return d(2 ** (horner.horner([1, 2, 1], arg, 3)) - 2)


def function_value(type, arg):
    if type == "1":
        return polynomial(arg)
    elif type == "2":
        return trigonometric(arg)
    elif type == "3":
        return exponential(arg)
    elif type == "4":
        return composite_function(arg)
    else:
        print("Incorrect function type provided.")


def derivative(type, x):
    if type == "1":
        return d(2 * x + 4)
    elif type == "2":
        return d(8 * np.cos(4 * x))
    elif type == "3":
        return d((2 ** x) * np.log(2))
    elif type == "4":
        return d(np.log(2)) * d(2) ** d((horner.horner([1, 2, 1], x, 3))) * d((2 * x + 2))
    else:
        print("Incorrect function type provided.")


def find_derivative_zero(a, b, type):
    x_values = np.linspace(a, b, 1000)
    for x in x_values:
        if d(derivative(type, x)) != d(0):
            return True
    return False
