import matplotlib.pyplot as plt
import numpy as np
import functions as f


def draw_function(type, a, b, bisection_root, secant_root):
    global function
    arguments = np.linspace(a, b, 1000)
    values = [f.function_value(type, x) for x in arguments]

    if type == '1':
        function = "x^2 + 4x - 5"
    elif type == '2':
        function = "2sin(4x)"
    elif type == '3':
        function = "2^x - 2"
    elif type == '4':
        function = "2^(x ^ 2 + 2x + 1) - 2"

    plt.plot(arguments, values, label=function)
    plt.scatter(bisection_root, f.function_value(type, bisection_root), color='red', marker='o',
                label="Root (bisection)")
    plt.scatter(secant_root, f.function_value(type, secant_root), color='blue', marker='x',
                label="Root (secant)")

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(function)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()
